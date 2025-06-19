#!/bin/bash

# Get today's date
today=$(date +%Y-%m-%d)

# Commit message with optional custom message
msg=${1:-"daily commit - $today"}

# Add everything
git add .

# Commit
git commit -m "$msg"

# Push
git push origin main
