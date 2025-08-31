from datetime import datetime

# README ni o‘qiymiz
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Hozirgi vaqt (UTC)
current_time = datetime.utcnow().strftime("%H:%M:%S")

# Yangi badge
new_badge = f"![Current Time](https://img.shields.io/badge/time-{current_time}%20UTC-brightgreen?style=for-the-badge&logo=clock)"

# README ichidagi eski badge’ni yangisiga almashtiramiz
new_readme = readme.split("<!--TIME_SECTION_START-->")[0] \
    + f"<!--TIME_SECTION_START-->\n{new_badge}\n<!--TIME_SECTION_END-->" \
    + readme.split("<!--TIME_SECTION_END-->")[1]

# Yangilangan README’ni saqlaymiz
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
