
queue = []


# 1. ENQUEUE
def enqueue():
    element = int(input("Enter element: "))
    queue.append(element)
    print("Element inserted")


# 2. DEQUEUE
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Deleted element:", queue.pop(0))


# 3. DISPLAY
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)


# 4. REVERSE QUEUE USING STACK
def reverse_queue():
    stack = []

    while len(queue) > 0:
        stack.append(queue.pop(0))

    while len(stack) > 0:
        queue.append(stack.pop())

    print("Reversed queue:", queue)


# FUNCTION TO ACCEPT ANOTHER QUEUE
def create_queue():
    q = []
    n = int(input("Enter number of elements: "))

    for i in range(n):
        element = int(input("Enter element: "))
        q.append(element)

    return q


# 5. MERGE TWO QUEUES
def merge_queue():
    q2 = create_queue()

    merged = queue + q2

    print("First Queue:", queue)
    print("Second Queue:", q2)
    print("Merged Queue:", merged)


# 6. CHECK IDENTICAL QUEUES
def identical_queue():
    q2 = create_queue()

    if queue == q2:
        print("Queues are identical")
    else:
        print("Queues are not identical")


# MAIN MENU
while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        reverse_queue()

    elif choice == 5:
        merge_queue()

    elif choice == 6:
        identical_queue()

    elif choice == 7:
        break

    else:
        print("Invalid choice")
