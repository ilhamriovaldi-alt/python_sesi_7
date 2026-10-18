from datetime import datetime
import time

now = datetime.now()
print("Current time using datetime:", now.strftime("%H:%M:%S"))

current_time = time.localtime()
print("Current time using time module:", time.strftime("%H:%M:%S", current_time))
