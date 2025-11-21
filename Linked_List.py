class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start of the linked list

    def insert_at_head(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # Node deleted
            prev = current
            current = current.next
        return False  # Node not found

    def search(self, data):
        """Search for a node with the given data."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Print all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(10)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)
    ll.insert_at_tail(40)
    ll.display()  
    print("Search 20:", ll.search(20))  
    print("Delete 20:", ll.delete(20))
    ll.display()  # 
