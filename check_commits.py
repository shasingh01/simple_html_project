import requests
import os

# Define the GitHub token, repo, and local file for commit tracking
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = "https://api.github.com/repos/shasingh01/simple_html_project/commits"
LOCAL_COMMIT_FILE = "/var/www/html/latest_commit.txt"

# Function to fetch the latest commit from the GitHub API
def get_latest_commit():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(GITHUB_REPO, headers=headers)
    if response.status_code == 200:
        latest_commit = response.json()[0]['sha']
        return latest_commit
    else:
        print("Failed to fetch latest commit. Status code:", response.status_code)
        return None

# Function to read the last saved commit SHA from the local file
def read_local_commit():
    if os.path.exists(LOCAL_COMMIT_FILE):
        with open(LOCAL_COMMIT_FILE, "r") as f:
            return f.read().strip()
    return None

# Function to write the new commit SHA to the local file
def write_local_commit(commit_sha):
    with open(LOCAL_COMMIT_FILE, "w") as f:
        f.write(commit_sha)

# Function to check if there's a new commit and trigger the deployment
def check_for_new_commits():
    latest_commit = get_latest_commit()
    local_commit = read_local_commit()

    print(f"Latest commit from GitHub: {latest_commit}")
    print(f"Local commit stored: {local_commit}")

    if latest_commit and latest_commit != local_commit:
        print("New commit detected!")
        write_local_commit(latest_commit)  # Update the local commit file
        os.system("/bin/bash /home/shasingh01/simple_html_project/deploy.sh")  # Trigger the deployment script
    else:
        print("No new commits.")

# Call the function to check for new commits
if __name__ == "__main__":
    check_for_new_commits()

