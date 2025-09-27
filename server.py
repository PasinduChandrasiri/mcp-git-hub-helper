import requests
from datetime import datetime, timedelta
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GitHelperMCP")

GITHUB_API = "https://api.github.com"

# =====================
# Tools
# =====================

@mcp.tool()
def repo_summary(username: str) -> list:
    """Return a summary of all public repos for a user"""
    url = f"{GITHUB_API}/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": f"Failed to fetch repos for {username}"}
    repos = response.json()
    return [
        {"name": r["name"], "stars": r["stargazers_count"], "forks": r["forks_count"], "private": r["private"]}
        for r in repos
    ]

@mcp.tool()
def check_readme(username: str) -> list:
    """Return repos missing README"""
    url = f"{GITHUB_API}/users/{username}/repos"
    response = requests.get(url)
    missing = []
    if response.status_code != 200:
        return {"error": f"Failed to fetch repos for {username}"}
    for r in response.json():
        readme_url = f"{GITHUB_API}/repos/{username}/{r['name']}/readme"
        r_resp = requests.get(readme_url)
        if r_resp.status_code == 404:
            missing.append(r['name'])
    return missing

@mcp.tool()
def check_license(username: str) -> list:
    """Return repos missing license"""
    url = f"{GITHUB_API}/users/{username}/repos"
    response = requests.get(url)
    missing = []
    if response.status_code != 200:
        return {"error": f"Failed to fetch repos for {username}"}
    for r in response.json():
        if r.get("license") is None:
            missing.append(r['name'])
    return missing

@mcp.tool()
def stale_issues(username: str, days: int = 30) -> dict:
    """Return issues older than X days"""
    url = f"{GITHUB_API}/users/{username}/repos"
    repos = requests.get(url).json()
    stale = {}
    cutoff = datetime.utcnow() - timedelta(days=days)
    for r in repos:
        issues_url = f"{GITHUB_API}/repos/{username}/{r['name']}/issues"
        issues = requests.get(issues_url).json()
        stale[r['name']] = [
            i['title'] for i in issues
            if 'pull_request' not in i and datetime.strptime(i['created_at'], "%Y-%m-%dT%H:%M:%SZ") < cutoff
        ]
    return stale

# =====================
# Resources
# =====================

@mcp.tool()
def get_github_user(username: str) -> dict:
    """Return JSON summary of GitHub user"""
    url = f"{GITHUB_API}/users/{username}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return {"error": f"User {username} not found"}
    return resp.json()

# =====================
# Prompts
# =====================

@mcp.tool()
def suggest_improvements_tool(username: str) -> str:
    """Generate suggestions to improve GitHub account"""
    missing_readme = check_readme(username)
    missing_license = check_license(username)
    suggestions = []
    if missing_readme:
        suggestions.append(f"Add README to repos: {', '.join(missing_readme)}")
    if missing_license:
        suggestions.append(f"Add license to repos: {', '.join(missing_license)}")
    if not suggestions:
        return f"Your GitHub account {username} looks good! ✅"
    return "Suggestions:\n" + "\n".join(suggestions)


# =====================
# Run Server
# =====================
if __name__ == "__main__":
    print("🚀 Starting Git Helper MCP Server...")
    mcp.run()
