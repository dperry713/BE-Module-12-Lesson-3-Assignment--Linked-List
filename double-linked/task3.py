# Create a new doubly linked list
dll = DoublyLinkedList()

# Insert elements into the list
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)

# Traverse the list
print("Doubly Linked List after insertion:")
dll.traverse_list()

# Delete a node
dll.delete_node(20)

# Traverse the list again
print("Doubly Linked List after deletion of 20:")
dll.traverse_list()

# Delete another node
dll.delete_node(10)

# Traverse the list again
print("Doubly Linked List after deletion of 10:")
dll.traverse_list()
