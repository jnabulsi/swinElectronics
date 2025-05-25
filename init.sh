#!/bin/bash

set -e

echo "[*] Starting dev environment setup..."

# Check for apt
if command -v apt &>/dev/null; then
  echo "[*] Detected apt - installing dependencies..."

  sudo apt update
  sudo apt install -y python3 python3-pip python3-venv curl

  # Install Node.js and npm if missing
  if ! command -v node &>/dev/null || ! command -v npm &>/dev/null; then
    echo "[*] Installing Node.js and npm..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt install -y nodejs
  fi
else
  echo "[*] 'apt' not found. Skipping dependency installation."
fi

# Setup backend
echo "[*] Setting up backend..."
cd backend

# Create virtual env if missing
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
BACKEND_PID=""

# Start FastAPI in background
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
deactivate
cd ..

# Setup frontend
echo "[*] Setting up frontend..."
cd frontend
npm install
npm run dev &
FRONTEND_PID=$!
cd ..

echo "[*] Go to localhost:8080 to see frontend"
echo "[*] CTL-C to stop dev servers"

# Handle shutdown
trap "echo 'Shutting down...'; kill $BACKEND_PID $FRONTEND_PID" SIGINT

# Keep script alive
wait
