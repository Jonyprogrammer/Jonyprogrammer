from datetime import datetime
import pytz
import os

# Toshkent vaqti (GMT+5)
tz = pytz.timezone("Asia/Tashkent")
now = datetime.now(tz)

current_time = now.strftime("%H:%M")
current_date = now.strftime("%Y-%m-%d")

# Badge faylini scripts ichida yaratish
badge_path = os.path.join(".github", "scripts", "TIME_BADGE.md")
badge_content = f"""
![Time Badge](https://img.shields.io/badge/Time-{current_time}-brightgreen?style=for-the-badge) ![Today Badge](https://img.shields.io/badge/Today-{current_date}-blue?style=for-the-badge)
"""

with open(badge_path, "w") as f:
    f.write(badge_content)

print(f"Badge yangilandi: {badge_path}")
