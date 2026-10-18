from datetime import date, datetime

first_date = date(2026, 10, 18)
second_date = date(2026, 10, 1)
difference = first_date - second_date
print("Date difference =", difference)
print("Type =", type(difference))

first_datetime = datetime(2026, 10, 18, 7, 0, 0)
second_datetime = datetime(2026, 10, 10, 5, 30, 0)
time_difference = first_datetime - second_datetime
print("Datetime difference =", time_difference)
