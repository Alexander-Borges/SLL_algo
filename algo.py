# 1. SLL Utilities
# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False 
        
    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# 2. Length
# Create a new SLL method length() that returns number of nodes in that list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count 

# 3. Display 
# Create display() that returns a string containing all list values. Build what you wish print(myList) did!
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)

# Bonus: Move Min to Front
# Create a standalone function that locates the minimum value in a linked list, and moves that node to the front of a list. Return the new list, with all nodes still present, and all(except for the new head node) in their original order. 
def move_min_to_front(sll):
    if not sll.head:
        return sll 
    
    current = sll.head
    min_node = sll.head
    prev = None 

    while current.next:
        if current.next.value < min_node.value:
            min_node = current.next
            prev = current
        current = current.next

    if min_node != sll.head:
        prev.next = min_node.next
        min_node.next = sll.head 
        sll.head = min_node

    return sll

# Bonus: SList: Move Max to Back
#Create a standalone function that locates the maximum value in a linked list, and moves that node to the back of the list. Return the new list, with all nodes still present, and all in their original order except for the node you moved to the end of the singly linked list.
def move_max_to_back(sll):
    if not sll.head:
        return sll
    
    current = sll.head
    max_node = sll.head
    prev = None

    while current.next:
        if current.next.value > max_node.value:
            max_node = current.next
            prev = current
        current = current.next

    if max_node != current:
        prev.next = max.mode.next
        current.next = max_node
        max_node.next = None

    return sll


myList = SLL()
myList.append(5)
myList.append(3)
myList.append(8)


print(myList.contains(3))  # Should print True
print(myList.contains(7))  # Should print False

length = myList.length()
print("Length of the list:", length) 

display_str = myList.display()
print("Linked List:", display_str)

print("Original List:", myList.display())

newList1 = move_min_to_front(myList)
print("After moving min to front:", newList1.display())

newList2 = move_max_to_back(newList1)
print("After moving max to back:", newList2.display())