CI/CD Pipeline Tool
This project demonstrates a simple CI/CD pipeline for an HTML project using Git, GitHub, Nginx, Python, Bash, and Cron jobs. The pipeline is designed to automatically deploy updates to a web server whenever new commits are pushed to a GitHub repository.

Table of Contents
Task 1: Create a Project Folder
Task 2: Set Up an EC2/Local Linux Instance with Nginx
Task 3: Write a Python Script to Check for New Commits
Task 4: Write a Bash Script to Deploy the Code
Task 5: Set Up Cron Job to Run the Python Script
Task 6: Test the Setup

Task 1: Create a Project Folder
Create a folder for your HTML project:

mkdir simple_html_project
cd simple_html_project


Initialize Git and Push to GitHub:

git init
git add index.html
git commit -m "Initial commit with simple HTML project"
git remote add origin https://github.com/yourusername/simple_html_project.git
git push -u origin new_test_branch

Task 2: Set Up an EC2/Local Linux Instance with Nginx
Install Nginx:

sudo apt update
sudo apt install nginx -y


Set up the HTML file:

echo "Hello World" > index.html
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 644 /var/www/html


Verify Nginx setup:

sudo systemctl restart nginx
curl 172.21.131.220

Task 3: Write a Python Script to Check for New Commits
Install Python and Pip:

sudo apt install python3-pip -y

Create a Python script (check_commits.py) to check for new commits using the GitHub API. The script should:

Fetch the latest commit from GitHub.
Compare it with the locally stored commit.
Trigger the deployment script if a new commit is found.

Task 4: Write a Bash Script to Deploy the Code
Create and make the deployment script executable:

chmod +x deploy.sh

deploy.sh should:

Pull the latest changes from the GitHub repository.
Copy the updated files to the Nginx web root.
Restart the Nginx service to apply the changes.

Task 5: Set Up Cron Job to Run the Python Script
Open the crontab:

crontab -e

Add a cron job to run the Python script at regular intervals:

*/5 * * * * /usr/bin/python3 /path/to/check_commits.py


Task 6: Test the Setup
Make a new commit in the GitHub repository.
Check if the deployment script is triggered automatically and if the changes are reflected on the web server.
Verify the setup using

curl 172.21.131.220



Conclusion
This pipeline allows for automatic deployment of an HTML project whenever new changes are pushed to the GitHub repository. The use of Python, Bash, and cron jobs ensures that the deployment process is automated and efficient.

NOTE: User can check script file for more info
