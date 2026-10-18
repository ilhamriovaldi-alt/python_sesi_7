import time

seconds = time.time()
print("Seconds since Unix epoch =", seconds)
print("Readable local time =", time.ctime(seconds))

local = time.localtime()
print("Local time structure =", local)
print("Formatted local time =", time.strftime("%d/%m/%Y %H:%M:%S", local))

utc = time.gmtime()
print("UTC time structure =", utc)
