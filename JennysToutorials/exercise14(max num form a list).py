numbers = input("enter the numbers whit a space:")
numbers = numbers.split()

count = 0

for number in numbers:
    count += 1

for i in range(0, count):
    numbers[i] = int(numbers[i])

print(numbers)

maximum = numbers[0]

for num in numbers:
    if num > maximum :
        maximum = num
print(maximum)

