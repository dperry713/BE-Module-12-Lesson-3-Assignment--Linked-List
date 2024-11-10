# Create a new singly linked list
sll = SinglyLinkedList()

# Insert elements into the list
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(40)

# Traverse the list
print("Linked List after insertion:")
sll.traverse_list()

# Delete a node
sll.delete_node(20)

# Traverse the list again
print("Linked List after deletion of 20:")
sll.traverse_list()

# Delete another node
sll.delete_node(10)

# Traverse the list again
print("Linked List after deletion of 10:")
sll.traverse_list()
