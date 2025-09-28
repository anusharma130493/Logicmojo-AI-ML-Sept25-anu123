# If No head
'''if No head:
    self.head = new_node
    new_node.next = self.head
    return

# At beginning
previous = self.head
current = previous
self.head = new_node
new_node.next = previous

while current.next != previous:
    current = current.next

current.next = new_node


# At End
if No head:
    self.head = new_node
    new_node.next = self.head
    return

previous = self.head
current = previous

while current.next != previous:
    current = current.next

current.next = new_node
new_node.next = previous
'''