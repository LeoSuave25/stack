class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(list_1, list_2):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode(0)
    # Create a pointer to traverse the merged list
    current = dummy
    
    # Create new nodes for the merged list
    while list_1 and list_2:
        if list_1.value <= list_2.value:
            current.next = ListNode(list_1.value)
            list_1 = list_1.next
        else:
            current.next = ListNode(list_2.value)
            list_2 = list_2.next
        current = current.next
    
    # Append the remaining nodes from the non-empty list to the merged list
    if list_1:
        current.next = list_1
    if list_2:
        current.next = list_2
    
    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Test the code with the given example
list_1 = ListNode(1)
list_1.next = ListNode(2)
list_1.next.next = ListNode(4)

list_2 = ListNode(1)
list_2.next = ListNode(3)
list_2.next.next = ListNode(4)

# Merge the two lists
merged_list = mergeTwoLists(list_1, list_2)

# Print the merged list
print("Merged List:")
current_merged = merged_list
while current_merged:
    print(current_merged.value, end=" -> ")
    current_merged = current_merged.next
print("None")
