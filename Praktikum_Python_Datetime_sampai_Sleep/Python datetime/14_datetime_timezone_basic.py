from datetime import datetime, timezone

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print("Local date and time:", local_now)
print("UTC date and time:", utc_now)
