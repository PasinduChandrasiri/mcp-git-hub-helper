# 🐙 GitHub Helper MCP Server

A Multi-Channel Prompt (MCP) server to analyze GitHub accounts, detect repository issues, and provide actionable improvement suggestions.  

---

## ✨ Features

- 📊 **Repo Summary:** List all public repositories with stars, forks, and visibility  
- 📝 **Check Missing README:** Identify repos without README files  
- ⚖️ **Check Missing License:** Identify repos missing licenses  
- 🕵️ **Stale Issues Detector:** Detect open issues older than a specified number of days  
- 👤 **GitHub User Info:** Fetch profile JSON data dynamically  
- 💡 **Improvement Suggestions:** Provides actionable recommendations for profile and repo enhancements  

---

## ⚡ Installation

- git clone https://github.com/PasinduChandrasiri/mcp-git-hub-helper
- cd git-helper-mcp
- uv add "mcp[cli]"
- pip install requests
- uv run server.py


Connect the server in Claude Desktop or any MCP-compatible client.

---

## 💻 Usage

### Tools:
- `repo_summary(username)`  
- `check_readme(username)`  
- `check_license(username)`  
- `stale_issues(username, days=30)`  
- `get_github_user(username)`  
- `suggest_improvements_tool(username)`  

### Example Queries:
- Use `repo_summary` for username `"PasinduChandrasiri"`  
- Use `check_readme` for username `"PasinduChandrasiri"`  
- Use `get_github_user` for username `"PasinduChandrasiri"`  
- Use `suggest_improvements_tool` for username `"PasinduChandrasiri"`  

---

## 🛠️ Tech Stack

- Python 3.10+ 🐍  
- FastMCP ⚡  
- MCP CLI 🛠️  
- GitHub API 🌐  
- Requests 💻  

---

Created by Pasindu Chandrasiri 
