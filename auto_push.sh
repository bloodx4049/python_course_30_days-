#!/bin/bash

REPO_DIR="/home/blood-x/Documents/ML/PYTHON/"
cd "$REPO_DIR"

# Check if there are changes
if ! git diff-index --quiet HEAD --; then
    git add .
    git commit -m "Auto-update: $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin master
    echo "✓ Code pushed at $(date '+%Y-%m-%d %H:%M:%S')"
else
    echo "No changes to commit"
fi
