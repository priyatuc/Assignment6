class Queue:
    def __init__(self):
        self.items = []  
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item. Raise error if queue is empty."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  # Remove the first element

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print("The queue is:", queue.items)
    print("Front item:", queue.front())  
    print("Queue size:", queue.size())   
    print("Dequeued item:", queue.dequeue())  
    print("Is queue empty?", queue.is_empty())  
