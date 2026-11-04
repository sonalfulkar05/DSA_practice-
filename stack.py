
# Stack Implementation

stack = []


# 1. PUSH
def push():
    element = int(input("Enter element to insert: "))
    stack.append(element)
    print("Element pushed successfully!")


# 2. POP
def pop():
    if len(stack) == 0:
        print("Stack is empty!")

    else:
        element = stack.pop()
        print("Deleted element:", element)


# 3. DISPLAY
def display():
    if len(stack) == 0:
        print("Stack is empty!")

    else:
        print("Stack elements (Top to Bottom):")

        for i in range(len(stack)-1, -1, -1):
            print(stack[i])


# 4. REVERSE STRING USING STACK
def reverse_string():

    string = input("Enter a string: ")

    temp = []

    # Push characters into stack
    for ch in string:
        temp.append(ch)

    reverse = ""

    # Pop characters from stack
    while len(temp) > 0:
        reverse = reverse + temp.pop()

    print("Original String:", string)
    print("Reversed String:", reverse)


# 5. REVERSE STACK USING ANOTHER STACK
def reverse_stack():

    if len(stack) == 0:
        print("Stack is empty!")

    else:
        temp = []

        # Transfer elements into another stack
        while len(stack) > 0:
            temp.append(stack.pop())

        # Transfer elements back
        stack.extend(temp)

        print("Stack reversed successfully!")


# MAIN MENU

while True:

    print("\n========== STACK MENU ==========")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using Another Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        reverse_string()

    elif choice == 5:
        reverse_stack()

    elif choice == 6:
        print("Program terminated!")
        break

    else:
        print("Invalid choice! Try again.")
