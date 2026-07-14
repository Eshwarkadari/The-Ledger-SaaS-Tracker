import os
import sqlite3
from datetime import date, datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "subtrack.db")

app = Flask(__name__)
app.secret_key = "dev-secret-change-in-production"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tool_name TEXT NOT NULL,
            monthly_cost REAL NOT NULL,
            renewal_date TEXT NOT NULL,
            billing_cycle TEXT NOT NULL DEFAULT 'monthly',
            owner TEXT,
            notes TEXT,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def days_until(iso_date_str):
    try:
        target = datetime.strptime(iso_date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    return (target - date.today()).days


def urgency_class(days):
    if days is None:
        return "unknown"
    if days < 0:
        return "overdue"
    if days <= 7:
        return "urgent"
    if days <= 30:
        return "soon"
    return "safe"


@app.route("/")
def dashboard():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM subscriptions ORDER BY renewal_date ASC"
    ).fetchall()
    conn.close()

    subs = []
    total_monthly = 0.0
    for r in rows:
        d = days_until(r["renewal_date"])
        sub = dict(r)
        sub["days_left"] = d
        sub["urgency"] = urgency_class(d)
        subs.append(sub)
        # normalize to monthly cost for the total burn figure
        if r["billing_cycle"] == "yearly":
            total_monthly += r["monthly_cost"] / 12
        else:
            total_monthly += r["monthly_cost"]

    upcoming = [s for s in subs if s["days_left"] is not None and s["days_left"] <= 30]
    upcoming.sort(key=lambda s: s["days_left"])

    tool_count = len(subs)
    yearly_burn = total_monthly * 12

    return render_template(
        "dashboard.html",
        subs=subs,
        upcoming=upcoming,
        total_monthly=total_monthly,
        yearly_burn=yearly_burn,
        tool_count=tool_count,
        today=date.today().strftime("%d %b %Y"),
    )


@app.route("/add", methods=["GET", "POST"])
def add_subscription():
    if request.method == "POST":
        tool_name = request.form.get("tool_name", "").strip()
        monthly_cost = request.form.get("monthly_cost", "").strip()
        renewal_date = request.form.get("renewal_date", "").strip()
        billing_cycle = request.form.get("billing_cycle", "monthly")
        owner = request.form.get("owner", "").strip()
        notes = request.form.get("notes", "").strip()

        if not tool_name or not monthly_cost or not renewal_date:
            flash("Tool name, cost, and renewal date are required.", "error")
            return redirect(url_for("add_subscription"))

        try:
            monthly_cost_val = float(monthly_cost)
        except ValueError:
            flash("Cost must be a number.", "error")
            return redirect(url_for("add_subscription"))

        conn = get_db()
        conn.execute(
            """INSERT INTO subscriptions
               (tool_name, monthly_cost, renewal_date, billing_cycle, owner, notes, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                tool_name,
                monthly_cost_val,
                renewal_date,
                billing_cycle,
                owner,
                notes,
                datetime.now().isoformat(),
            ),
        )
        conn.commit()
        conn.close()
        flash(f"Logged {tool_name} to the ledger.", "success")
        return redirect(url_for("dashboard"))

    return render_template("add.html")


@app.route("/delete/<int:sub_id>", methods=["POST"])
def delete_subscription(sub_id):
    conn = get_db()
    conn.execute("DELETE FROM subscriptions WHERE id = ?", (sub_id,))
    conn.commit()
    conn.close()
    flash("Entry removed from the ledger.", "success")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)