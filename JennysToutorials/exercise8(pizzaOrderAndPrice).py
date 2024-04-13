print("price for pizzas :")
print("Small Pizza --- 100 rupee")
print("Medium Pizza --- 200 rupee")
print("Large Pizza --- 300 rupee")
print()
print("Peperoni price :")
print("for small pizza --- 30 rupee")
print("for medium pizza --- 50 rupee")
print("for large pizza --- 60 rupee")
print()
print("prize for extra cheese --- 20 rupee")

order = input("Enter the pizza type you want to order :").lower()
pizzaType = "".join(order.split())

if pizzaType == "smallpizza" or pizzaType == "small":
    amount = 0
    amount += 100
    peperoni = input("Do you want to add peperoni to your pizza ?").lower()
    if peperoni == "yes":
        amount += 30
        cheese = input("Do you want to add extra Cheese to your pizza ?").lower()
        if cheese == "yes":
            amount += 20
            print(f"the total amount to pay for your order is : {amount}")
        elif cheese == "no":
            amount = 130
            print(f"the total amount to pay for your order is : {amount}")
        else:
            print("invalid input")
    elif peperoni == "no":
        amount = 100
        cheese = input("Do you want to add extra Cheese to your pizza ?").lower()
        if cheese == "yes":
            amount += 20
            print(f"the total amount to pay for your order is : {amount}")
        elif cheese == "no":
            amount = 100
            print(f"the total amount to pay for your order is : {amount}")
        else:
            print("invalid input")
    else:
        print("invalid input")


elif pizzaType == "mediumpizza" or pizzaType == "medium":
    amount = 0
    amount += 200
    peperoni = input("Do you want to add peperoni to your pizza ?").lower()
    if peperoni == "yes":
        amount += 50
        cheese = input("Do you want to add extra Cheese to your pizza ?").lower()
        if cheese == "yes":
            amount += 20
            print(f"the total amount to pay for your order is : {amount}")
        elif cheese == "no":
            amount = 250
            print(f"the total amount to pay for your order is : {amount}")
        else:
            print("invalid input")
    elif peperoni == "no":
        amount = 200
        cheese = input("Do you want to add extra Cheese to your pizza ?").lower()
        if cheese == "yes":
            amount += 20
            print(f"the total amount to pay for your order is : {amount}")
        elif cheese == "no":
            amount = 200
            print(f"the total amount to pay for your order is : {amount}")
        else:
            print("invalid input")
    else:
        print("invalid input")


elif pizzaType == "largepizza" or pizzaType == "large":
    amount = 0
    amount += 300
    peperoni = input("Do you want to add peperoni to your pizza ?").lower()
    if peperoni == "yes":
        amount += 60
        cheese = input("Do you want to add extra Cheese to your pizza ?").lower()
        if cheese == "yes":
            amount += 20
            print(f"the total amount to pay for your order is {amount}")
        elif cheese == "no":
            amount = 360
            print(f"the total amount to pay for your order is : {amount}")
        else:
            print("invalid input")
    elif peperoni == "no":
        amount = 300
        cheese = input("Do you want to add extra Cheese to your pizza ?").lower()
        if cheese == "yes":
            amount += 20
            print(f"the total amount to pay for your order is : {amount}")
        elif cheese == "no":
            amount = 300
            print(f"the total amount to pay for your order is : {amount}")
        else:
            print("invalid input")
    else:
        print("invalid input")

else:
    print("invalid input")

