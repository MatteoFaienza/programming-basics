# I ask the user to enter the date
day=int(input('Enter the day ')) 
month=int(input('Enter the month '))
year=int(input('Enter the year '))

print('The next day is')
# With the use of nested conditions, calculation the next day after the one entered by the user
if day == 28 :
    if month == 2 :
        print(f"{day-27:02d}",'/',f"{month+1:02d}",'/',year)

elif day == 30 :
    if month == 4 or month == 6 or month == 9 or month == 11:
        print(f"{day-29:02d}",'/',f"{month+1:02d}",'/',year)

elif day == 31 :
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 10 :
        print(f"{day-30:02d}",'/',f"{month+1:02d}",'/',year)
    elif month == 12 :
        print (f"{day-30:02d}",'/',f"{month-11:02d}",'/',year+1)    
else :
    print( f"{day+1:02d}",'/',f"{month:02d}",'/',year) 