print("Let\'s check if the year is a Leap year or not ")
print()
print("A leap year occurs after every 4 years, and it has 366 day rather than 365 days.")
print("If a year is divisible by 100 and 400 then it is a leap year else not")
print()
year = int(input("Enter the Year :"))

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"The year {year} is a Leap year ")
else:
    print(f"The year {year} is not a Leap year ")
