# 🔍 GitHub User Events Fetcher (Python)

A simple Python script that uses the **GitHub REST API** to fetch and display the latest public events of any GitHub user — such as pushes, forks, stars, and more.

---

## 🚀 Features
- Fetches recent activity (events) of any GitHub user  
- Displays event type, repo name, and timestamp  
- Uses **GitHub API v3**  
- Supports **token authentication** for higher rate limits  

---

## 🧰 Requirements
Make sure you have:
- Python 3.8 or higher
- `requests` library

Install dependencies:
```bash
pip install requests
```
1. Clone the Repository
Copy code
```
git clone https://github.com/Dhairya1890/<CLI-Github-Stalker>.git
cd <CLI-Github-Stalker>
```
2. Create a GitHub Access Token
Go to ```https://github.com/settings/tokens```

Click "Generate new token (classic/fine-grained)"

Give it at least these scopes:
<ul>
<li>read:user</li>
<li>events</li>
<li>repo (optional, if accessing private repos)</li>
</ul>

Copy your generated token.

3. Set Your Token as Environment Variable
On Windows PowerShell:
powershell
Copy code
```
$env:github_access_token = "your_token_here"
```
On Linux/Mac:
```
Copy code
export github_access_token="your_token_here"
```
▶️ Run the Script
Run the program:

Copy code
```
python github_events.py
```
Then enter any GitHub username when prompted:

## 🧠 Troubleshooting

| Problem | Possible Cause | Solution |
|----------|----------------|-----------|
| `KeyError: 'github_access_token'` | Environment variable not set | Set the token using:<br>`export github_access_token="your_token_here"` (Linux/Mac) or `$env:github_access_token = "your_token_here"` (Windows PowerShell) |
| `403: rate limit exceeded` | Too many unauthenticated requests | Use a valid GitHub access token to increase the limit |
| `404: Not Found` | Invalid or misspelled username | Check the GitHub username and try again |
| `401: Bad credentials` | Invalid token or expired | Regenerate a new token from GitHub and update your environment variable |
| `requests.exceptions.ConnectionError` | No internet connection or blocked API call | Check your internet and retry |

<hr>
📜 License
This project is open-source and available under the MIT License.
<hr>
**Created as a project from [Roadmap.sh](https://roadmap.sh/projects/github-user-activity)
