from datetime import datetime

# Vaqt formatini oling
current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Placeholder ichini yangilaymiz
new_readme = readme.split("<!--TIME_SECTION_START-->")[0] \
    + f"<!--TIME_SECTION_START-->\n{current_time}\n<!--TIME_SECTION_END-->" \
    + readme.split("<!--TIME_SECTION_END-->")[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
