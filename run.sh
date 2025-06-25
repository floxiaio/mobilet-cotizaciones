#!/bin/bash

# Install Node.js dependencies
npm install

# Install Python dependencies (if needed)
# pip install -r requirements.txt

# Run lite-server to serve the landing page
npm run start &

# Run Flask server if needed (uncomment if using server.py)
# python server.py &
