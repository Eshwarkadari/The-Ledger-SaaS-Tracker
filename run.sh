#!/bin/bash
echo "🚀 Starting The Ledger..."
python -c "from app import init_db; init_db()"
echo "✅ Database ready!"
echo "🌐 Open http://localhost:5000"
python app.py
