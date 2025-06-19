#!/bin/bash

# Prompt for file name
read -p "📄 Enter filename (with path from repo root): " file

# Get today's date
today=$(date +"%Y-%m-%d")

# Git commands
git add "$file"
git commit -m "Add solution: $file ($today)"
git push origin main
