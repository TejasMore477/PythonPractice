height = round(float(input("Enter Your Height In Meters :")),2)
print()

rupee = 0

if height >= 1.3:
    print("You can enjoy the ride!!")
    print()

    age = int(input("Please Enter Your Age :"))

    if age < 18:
        print("You Will Have To Pay Rupees 60 Per Ride")
        rupee = 60

    else:
        print("You Will Have To Pay Rupees 120 Per Ride")
        rupee = 120

    print()
    takePhoto = input("Do You Want To Take A Photo ? ").lower()
    print()

    if takePhoto == "yes":
        print("You Will Have To Pay Extra 50 Rupees For Photo")
        rupee += 50
        print(f"Your Total Amount To Pay For The Ride Is Rupee : {rupee}")

    elif takePhoto == "no":
        print(f"Your Total Amount To Pay For The Ride Is Rupee : {rupee}")

    else:
        print("Invalid Inputs")

else:
    print(" Sorry You can't enjoy the ride!! Come Next Year")

