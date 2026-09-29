#Find the smallest and Largest Element: Write a program to accept N integers into an array and find and display the largest element, second largest element, smallest element, second smallest element present in the array. 
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Find the largest and smallest elements
largest = max(arr)
smallest = min(arr)

# Find the second largest and second smallest elements
arr_unique = list(set(arr))
arr_unique.sort()

if len(arr_unique) >= 2:
    second_largest = arr_unique[-2]
    second_smallest = arr_unique[1]
else:
    second_largest = None
    second_smallest = None

# Display the results
print("Largest element:", largest)
print("Second largest element:", second_largest)
print("Smallest element:", smallest)
print("Second smallest element:", second_smallest)