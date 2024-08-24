#!/bin/bash

cd "$(dirname "$0")"

git add .

git commit -m "Saturday Monring Commits on $(date +'%Y-%m-%d')"

git push origin main
