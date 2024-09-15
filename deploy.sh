#!/bin/bash

# Set the directory for the project
PROJECT_DIR="/var/www/html"

# Go to the project directory
cd $PROJECT_DIR

# Pull the latest changes from GitHub
sudo git pull origin master  # Make sure to use the correct branch

# Restart Nginx to apply the changes
sudo systemctl restart nginx

echo "Deployment complete."


