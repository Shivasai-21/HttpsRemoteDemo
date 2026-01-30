import requests

# Replace with your GitHub username and personal access token
USERNAME = "your-github-username"
TOKEN = "your-personal-access-token"

# GitHub API endpoint
url = f"https://api.github.com/users/{USERNAME}/repos"

# Make the request with authentication
response = requests.get(url, auth=(USERNAME, TOKEN))

if response.status_code == 200:
    repos = response.json()
    print("Your repositories:")
    for repo in repos:
        print(f"- {repo['name']} (URL: {repo['html_url']})")
else:
    print(f"Error: {response.status_code} - {response.text}")
