#!/bin/bash

# Set the directory for the project
PROJECT_DIR="/home/shasingh01/simple_html_project"

# Go to the project directory
cd $PROJECT_DIR || { echo "Error: Could not change directory to $PROJECT_DIR"; exit 1; }

# Ensure we are in a valid Git repository
if [ ! -d ".git" ]; then
  echo "Error: Not a Git repository!"
  exit 1
fi

# Pull the latest changes from GitHub
sudo git pull origin new_test_branch  # Make sure to use the correct branch

# Copy the updated index.html to /var/www/html
sudo cp index.html /var/www/html/index.html


# Restart Nginx to apply the changes
sudo systemctl restart nginx

echo "Deployment complete."


