from datetime import datetime

now = datetime.now()
print("Time:", now.strftime("%H:%M:%S"))
print("Month/day/year:", now.strftime("%m/%d/%Y, %H:%M:%S"))
print("Day/month/year:", now.strftime("%d/%m/%Y, %H:%M:%S"))
