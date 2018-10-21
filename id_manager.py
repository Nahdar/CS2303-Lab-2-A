

# Creating Node class
class Node:
    item = -1
    next = None

    def __init__(self, item, next):
        self.item = item
        self.next = next


# Bubble Sort starts
def bubbleSort(head):

    counter = 0
    holder = head

    #Counting items in list
    while head is not None:
        counter = counter + 1
        head = head.next

    head = holder

    #Bubble sort
    for i in range(counter):
        head = holder
        for j in range(0, counter - i - 1):
            if head.item > head.next.item:
                head.item, head.next.item = head.next.item, head.item
            head = head.next
        head = head.next

    return holder


# Merge Sort starts
def mergeSortLinkedList(A):
    if A is None or A.next is None:
        return A

    leftHalf, rightHalf = splitTheList(A)

    left = mergeSortLinkedList(leftHalf)
    right = mergeSortLinkedList(rightHalf)

    return mergeTheLists(left, right)


def splitTheList(sourceList):
    if sourceList == None or sourceList.next == None:
        leftHalf = sourceList
        rightHalf = None

        return leftHalf, rightHalf

    else:
        midPointer = sourceList
        frontRunner = sourceList.next
        # totalLength += 1        - This is unnecessary

        while frontRunner != None:
            frontRunner = frontRunner.next

            if frontRunner != None:
                frontRunner = frontRunner.next
                midPointer = midPointer.next

    leftHalf = sourceList
    rightHalf = midPointer.next
    midPointer.next = None

    return leftHalf, rightHalf


def mergeTheLists(leftHalf, rightHalf):
    fake_head = Node(None, None)
    curr = fake_head

    while leftHalf and rightHalf:
        if leftHalf.item < rightHalf.item:
            curr.next = leftHalf
            leftHalf = leftHalf.next

        else:
            curr.next = rightHalf
            rightHalf = rightHalf.next

        curr = curr.next

    if leftHalf == None:
        curr.next = rightHalf

    elif rightHalf == None:
        curr.next = leftHalf

    return fake_head.next


# Solution 1 starts
def solution1(head):

    while head is not None:
        holder = head.next
        while holder is not None:
            # print("Head: " + head.item)
            # print("Holder: " + holder.item)
            if holder.item == head.item:
                print("Duplicate: " + str(holder.item))
            holder = holder.next
        head = head.next


# Solution 2 starts
def solution2(head):

    holder = bubbleSort(head)

    #Checking for Duplicates
    while holder.next is not None:
        if holder.item == holder.next.item:
            print("Duplicate:" + str(holder.item))
        holder = holder.next


#Solution 3 starts
def solution3(head):

    head = mergeSortLinkedList(head)

    #Checking for Duplicates
    while head.next is not None:
        if head.item == head.next.item:
            print("Duplicate:" + str(head.item))
        head = head.next


#Solution 4 starts
def solution4(head):

    holder = head
    largest = head.item

    #Checking for biggest item
    while head is not None:
        if head.item > largest:
            largest = head.item
        head = head.next

    seen = [False] * (largest + 1)

    #Checking for duplicates
    while holder is not None:
        if seen[holder.item] is True:
            print("Duplicate: " + str(holder.item))
        seen[holder.item] = True
        holder = holder.next



# Main method begins
# Initializing files & variables
file1 = open("activision.txt")
file2 = open("vivendi.txt")
list = None
holder = None
holder2 = None

# Creating the list
for line in file1:
    #holder2 = Node(str.strip(line), holder)
    holder2 = Node(int(line), holder)
    holder = holder2

for line in file2:
    holder2 = Node(int(line), holder)
    holder = holder2

list = holder

# Implement the solution
solution2(list)

