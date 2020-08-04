class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            current = current.next

        return None 

    def add_to_head(self, node):
        # Set our `next` to be our head, and make the new head the Node.
        node.next = self.head
        self.head = node

    def delete(self, value):
        # Set the current selected value, and begin traversing.
        # (Start with the head)
        current = self.head
        if current.value == value:
            self.head = self.head.next
            return current

        # Set `prev` to be our current value, and the new
        # current value should be our next value.
        prev = current
        current = current.next
        
        # So long as a current value exists...
        while current:
            # If it's our value, delete node.
            if current.value == value:
                prev.next = current.next
                return current
            else:  # If it isn't...
                # Continue traversing our linked list.
                prev = prev.next
                current = current.next
        return None