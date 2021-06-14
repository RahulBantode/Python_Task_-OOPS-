#10.Write A Python Program to display the current date , time, day.

#to get current date and time using python we have to import the package like datetime

from datetime import date

current=datetime.now()
#using now we are getting current date and time

print("The current date and time or day =")

print("Time = ",current)

print("Day = ",current.day)

print("Year = ",current.year)

print("Month = ",current.month)

print("ToDay = ",current.today)