# Deletion

def delete(self, key):

    if No head:
        return

    # delete head
    previous = self.head

    if previous.data == key:
        self.head = previous.next
        current = self.head
        while current.next != previous:
            current = current.next
        current.next = self.head
        return


    # delete last Node
    previous = self.head
    current = previous

    while current.data != key and current.next != previous:
        temp = current
        current = current.next

    temp.next = previous


    # In Mid
    while current.data != key and current.next != previous:
        temp = current
        current = current.next

    temp.next = current.next
