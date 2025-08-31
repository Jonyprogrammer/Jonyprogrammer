import os
import requests

username = "Jonyprogrammer"  
rfile = "README.md"

# GitHub API orqali public repolarni olish
url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
repos = requests.get(url).json()

cards = []
for repo in repos:
    repo_name = repo["name"]
    card = f'[![{repo_name}](https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={repo_name}&theme=radical)](https://github.com/{username}/{repo_name})'
    cards.append(card)

repos_markdown = "\n\n".join(cards)

# README yangilash
start = "<!-- REPO-LIST:START -->"
end = "<!-- REPO-LIST:END -->"

if os.path.exists(rfile):
    s = open(rfile, "r", encoding="utf-8").read()
else:
    s = ""

if start in s and end in s:
    pre, rest = s.split(start, 1)
    _, post = rest.split(end, 1)
    new = pre + start + "\n" + repos_markdown + "\n" + end + post
else:
    new = s + "\n\n" + start + "\n" + repos_markdown + "\n" + end + "\n"

open(rfile, "w", encoding="utf-8").write(new)
print("README updated with stats cards ✅")
