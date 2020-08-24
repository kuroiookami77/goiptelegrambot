#!/bin/bash
# скрипт для пуша в мастер

echo "Push to git"

git add .
git commit -m "new version $(date)"
git push -f origin master

