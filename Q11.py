#count substring in a string
string = input("Enter the main string: ")
substring = input("Enter the substring: ")

count = 0
positions = []

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        count += 1
        positions.append(i)

print("Number of occurrences:", count)
print("Positions:", positions)