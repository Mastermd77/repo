from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print(new_date)



today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)



now = datetime.now()
clean_now = now.replace(microsecond=0)
print(clean_now)




date1 = datetime(2026, 2, 26, 12, 0, 0)
date2 = datetime(2026, 2, 25, 8, 30, 0)

difference = date1 - date2
seconds = difference.total_seconds()
print(seconds)