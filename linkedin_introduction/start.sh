#!/usr/bin/env bash
echo "🚀 Setting up and running Developer CV Streamlit app..."

# Create venv if not exists
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activate venv
source .venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Run Streamlit
streamlit run streamlit_app.py
