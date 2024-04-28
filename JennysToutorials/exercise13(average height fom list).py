heights = (input("enter the heights seperated by space:"))
height = heights.split()
print(height)
count = 0

for ele in height:
    count = count + 1
    
for i in range(0, count):
    height[i] = int(height[i])
    
print(height)

total = 0
avg = 0

for i in height:
    total = total + i

avg  = round(total/count)
print(avg)