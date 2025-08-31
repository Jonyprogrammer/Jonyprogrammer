import os

rfile = 'README.md'
repos = open('repos.md','r',encoding='utf-8').read().strip()
start = '<!-- REPO-LIST:START -->'
end = '<!-- REPO-LIST:END -->'

if os.path.exists(rfile):
    s = open(rfile,'r',encoding='utf-8').read()
else:
    s = ""

if start in s and end in s:
    pre,rest = s.split(start,1)
    _,post = rest.split(end,1)
    new = pre + start + "\n" + repos + "\n" + end + post
else:
    new = s + "\n\n" + start + "\n" + repos + "\n" + end + "\n"

open(rfile,'w',encoding='utf-8').write(new)
print("✅ README updated with repo list")
