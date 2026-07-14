# 📒 The Ledger — SaaS Subscription Tracker

> A lightweight, self-hosted **SaaS subscription tracker** built for small Indian startups and SMEs who lose money to forgotten renewals, duplicate tools, and unused seats.

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)

---

## 💡 The Problem

Startups accumulate SaaS subscriptions across teams with no central owner. This leads to:

- 💸 **Forgotten renewals** that auto-charge before anyone notices
- 🔁 **Duplicate tools** bought independently by different teams
- 👻 **Unused seats** for employees who've left
- 📊 **No single view** of total monthly software burn

> Inspired by [Razorpay's "Fix My Itch"](https://razorpay.com/m/fix-my-itch/) initiative.

---

## ✨ Features

- 📊 **Live Dashboard** — monthly & annualized burn total at a glance
- 📅 **30-day renewal timeline** — never miss a renewal again
- 📋 **Full ledger view** — every subscription with owner, cost, notes
- 🔴 **Urgency indicators** — Overdue / Urgent / Soon / Safe
- ➕ **Add/Delete** subscriptions easily
- 🗄️ **SQLite database** — zero config, file-based, portable
- 🚀 **Deploy to Render** in 2 minutes (free)

---

## 🗂️ Project Structure

```
The-Ledger-SaaS-Tracker/
├── app.py                    # Flask app — all routes & DB logic
├── templates/
│   ├── base.html             # Base layout
│   ├── dashboard.html        # Main dashboard
│   └── add.html              # Add subscription form
├── static/
│   └── style.css             # Styles
├── requirements.txt          # Flask + Gunicorn
├── Procfile                  # For Render deployment
├── render.yaml               # One-click Render deploy
├── .devcontainer/
│   └── devcontainer.json     # GitHub Codespaces config
├── run.sh                    # Quick start script
└── README.md
```

---

## 🚀 Run Locally (3 steps)

```bash
# 1. Clone
git clone https://github.com/Eshwarkadari/The-Ledger-SaaS-Tracker
cd The-Ledger-SaaS-Tracker

# 2. Install
pip install -r requirements.txt

# 3. Run
python app.py
```

Open **http://localhost:5000** 🎉

---

## ▶️ Run in GitHub Codespaces (Zero Install!)

1. Go to this repo on GitHub
2. Click green **"Code"** button → **"Codespaces"** tab
3. Click **"Create codespace on main"**
4. Wait 1 minute → VS Code opens in browser
5. In terminal: `python app.py`
6. Click **"Open in Browser"** → done! ✅

---

## 🌐 Deploy FREE on Render

1. Fork this repo
2. Go to **render.com** → New → Web Service
3. Connect your forked repo
4. Render reads `render.yaml` automatically
5. Click **Deploy** → live in 2 minutes!

---

## 📊 Dashboard Preview

```
┌─────────────────────────────────────────────────────┐
│  📒 The Ledger              Today: 12 Jul 2026      │
├──────────┬──────────────┬───────────┬───────────────┤
│  Tools   │ Monthly Burn │ Yearly    │  Due in 30d   │
│    8     │   ₹12,450   │ ₹1,49,400 │      3        │
├─────────────────────────────────────────────────────┤
│  Tool         │ Cost    │ Renewal   │ Status        │
│  Notion       │ ₹800    │ Jul 15    │ 🔴 URGENT    │
│  Slack        │ ₹2,200  │ Jul 28    │ 🟡 SOON      │
│  GitHub       │ ₹500    │ Aug 10    │ 🟢 SAFE      │
│  Figma        │ ₹1,500  │ Sep 01    │ 🟢 SAFE      │
└─────────────────────────────────────────────────────┘
```

---

## 🗺️ Roadmap

- [x] Manual subscription logging + dashboard
- [x] Renewal timeline (30-day lookahead)
- [x] Urgency indicators (Overdue/Urgent/Soon/Safe)
- [ ] Email-forward ingestion (auto-populate from renewal emails)
- [ ] Monthly reminder nudges via WhatsApp/Email
- [ ] Account Aggregator (AA) integration for bank-linked data
- [ ] Multi-tenant support for multiple organizations

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| Database | SQLite (zero-config) |
| Frontend | Jinja2 + HTML/CSS |
| Deployment | Render (free tier) |
| Dev Environment | GitHub Codespaces |

---

## 👨‍💻 Author

**Kadari Eshwar** — B.Tech ECE, CMR College of Engineering and Technology
[GitHub](https://github.com/Eshwarkadari) | [LinkedIn](https://www.linkedin.com/in/eshwar-kadari-134aa4278)
