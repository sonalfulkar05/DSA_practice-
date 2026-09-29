n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

total = 0

for num in arr:
    total += num

print("Sum of array elements =", total)