list1 = ["☠", "☠", "☠"]
list2 = ["☠", "☠", "☠"]
list3 = ["☠", "☠", "☠"]

matrix = [list1, list2, list3]

location = input("enter the location to target in the matrix :")
rowPosition = int(location[0])
columPosition = int(location[1])

matrix[rowPosition -1][columPosition -1] = "X"

print(f"{list1}\n{list2}\n{list3}")