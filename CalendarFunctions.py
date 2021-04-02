# -*- coding: utf-8 -*-

import calendar

#Show the monthly calendar for the year and month March 2021
mar = calendar.TextCalendar(calendar.SUNDAY)
mar.prmonth(2021, 3)

#Show the monthly calendar for the year and month March 1990
birthday = calendar.TextCalendar(calendar.MONDAY)
birthday.prmonth(1990, 3)

#count leap years between two years
leaps = calendar.leapdays(1984,2021)
print(leaps)



#interactive leap year calculator
print("\n\n Leap Year Calculator\n")

year1 = int(input("Enter the first year: "))
year2 = int(input("And a second year: "))

leapResult = calendar.leapdays(year1, year2)

print("\n\n The number of leap years between ", year1, " and ", year2, " is ", leapResult)




#Display all the months of a year in a full calendar
dispYear = int(input("\nSelect a year to display a full calendar: "))
print(calendar.prcal(dispYear))


#for loop to count days
for i in mar.itermonthdays(2021, 3):
    print(i)
    
#print month names    
for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)
    

#write the calendar functions to a webpage
page = open("calendar.html", "w")
c = calendar.HTMLCalendar(calendar.MONDAY)
page.write(c.formatmonth(2021, 3))
page.close()

#write a webpage after user input
pageYear = int(input("\nEnter the year to display as a webpage: "))
inputpage = open("inputcalendar.html", "w")
inputpage.write(calendar.HTMLCalendar(calendar.MONDAY).formatyear(pageYear))
inputpage.close()
