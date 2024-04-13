import random

strings = input("Enter the name separated by commas :")
list1 = strings.split(",")
length = len(list1)
num = random.randint(0, length-1)
print(f"{list1[num]} will pay today's bill")
