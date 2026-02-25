from datetime import datetime, timedelta
import pytz

# 1
now = datetime.now()
print(now)

# 2
birthday = datetime(2007, 7, 27)
print(birthday)

# 3
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))

# 4
future = now + timedelta(days=7)
print(future)
difference = future - now
print(difference)

# 5
if birthday < now:
    print("Birthday is in the past")

# 6
timezone = pytz.timezone("Asia/Almaty")
local_time = datetime.now(timezone)
print(local_time)