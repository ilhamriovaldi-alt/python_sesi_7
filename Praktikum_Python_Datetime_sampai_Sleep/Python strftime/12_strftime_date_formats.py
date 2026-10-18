from datetime import date

today = date.today()
print("dd/mm/YYYY:", today.strftime("%d/%m/%Y"))
print("Month day, year:", today.strftime("%B %d, %Y"))
print("mm/dd/yy:", today.strftime("%m/%d/%y"))
print("Abbreviated month:", today.strftime("%b-%d-%Y"))
