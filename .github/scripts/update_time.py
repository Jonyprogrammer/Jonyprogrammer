from datetime import datetime
import pytz
import os
import re

# Toshkent vaqti (GMT+5)
tz = pytz.timezone("Asia/Tashkent")
now = datetime.now(tz)

current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")

# Timestamp qo‘shib cache muammosini oldini olish
timestamp = int(now.timestamp())

# README fayli yo‘li
readme_path = "README.md"

# Badge yangilanish qismi
new_badge = f"![Current Time](https://img.shields.io/badge/time-{current_time}%20GMT%2B5-brightgreen?style=for-the-badge&logo=clock&cacheSeconds={timestamp})"

# README faylini o‘qib, badge qismni yangilash
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# TIME_SECTION_START va TIME_SECTION_END orasini yangilash
pattern = r"(<!--TIME_SECTION_START-->)(.*?)(<!--TIME_SECTION_END-->)"
new_content = re.sub(pattern, fr"\1\n{new_badge}\n\3", content, flags=re.DOTALL)

# README faylini yozish
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"README.md ichidagi vaqt badge yangilandi: {current_time}, {current_date}")
