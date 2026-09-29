# Search an Element: Write a program to accept N integers into an array and search for a given number. Display an appropriate message indicating whether the number is present in the array or not and also display its position. 
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search_num = int(input("Enter the number to search: "))
found = False
position = -1

for i in range(n):
    if arr[i] == search_num:
        found = True
        position = i
        break

if found:
    print(f"Number {search_num} is present in the array at position {position}")
else:
    print(f"Number {search_num} is not present in the array")