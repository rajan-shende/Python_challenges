import calendar
# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

month = int(input("Enter a month"))
year = int(input("Enter a year"))

print(calendar.monthcalendar(year, month))
print(calendar.month(year, month))