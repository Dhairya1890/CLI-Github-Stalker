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
⚙️ Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2. Create a GitHub Access Token
Go to https://github.com/settings/tokens

Click "Generate new token (classic)"

Give it at least these scopes:

read:user

repo (optional, if accessing private repos)

Copy your generated token.

3. Set Your Token as Environment Variable
On Windows PowerShell:
powershell
Copy code
$env:github_access_token = "your_token_here"
On Linux/Mac:
bash
Copy code
export github_access_token="your_token_here"
▶️ Run the Script
Run the program:

bash
Copy code
python github_events.py
Then enter any GitHub username when prompted:

yaml
Copy code
Enter Username: Dhairya1890
PushEvent on Dhairya1890/AI-Notes at 2025-10-30T11:25:45Z
WatchEvent on Dhairya1890/Portfolio at 2025-10-29T14:32:10Z
🧩 Code Example
python
Copy code
import requests
import os

token = os.environ['github_access_token']
username = input("Enter Username: ")

BASE_URL = "https://api.github.com"
headers = {
    'Authorization': f'token {token}',
    "Accept": "application/vnd.github.v3+json"
}

url = f"{BASE_URL}/users/{username}/events"
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("❌ Error:", response.status_code, response.text)
    exit()

events = response.json()
for e in events[:5]:
    print(f"{e['type']} on {e['repo']['name']} at {e['created_at']}")
🧠 Troubleshooting
Problem	Cause	Solution
KeyError: 'github_access_token'	Token not set in environment	Set it again using export or $env:
403: rate limit exceeded	No authentication / too many requests	Use a valid token
404: Not Found	Wrong username	Check spelling of username

📜 License
This project is open-source and available under the MIT License.
