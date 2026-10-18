import time

time_string = "14 July, 2023"
result = time.strptime(time_string, "%d %B, %Y")

print("Original string =", time_string)
print("Parsed time =", result)
