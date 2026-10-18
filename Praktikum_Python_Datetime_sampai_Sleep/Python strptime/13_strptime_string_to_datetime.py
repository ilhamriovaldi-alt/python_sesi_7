from datetime import datetime

date_string = "25 December, 2022"
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("Original string =", date_string)
print("Datetime object =", date_object)
print("Object type =", type(date_object))
