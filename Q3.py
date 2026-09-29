#. Count Even and Odd Numbers: Write a program to accept N integers into an array and count and display the number of even and odd elements present in the array. 
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

even_count = 0
odd_count = 0

for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)