class Queue:
    """
    The queue data structure and it's methods
    """

    def __init__(self, Bi):
        """Initializing the queue with the specified buffer size"""
        self.items = []
        self.buffer_size = Bi


    def is_empty(self):
        """Check if the queue is empty"""
        return self.items == []


    def enqueue(self, item):
        """Enqueue the given item to the queue"""
        self.items.insert(0,item)


    def dequeue(self):
        """Simply returns the queue"""
        return self.items


    def size(self):
        """Returns the size of the queue"""
        return len(self.items)


    def is_queue_full(self):
        """Returns true if the queue has reached it's buffer size"""
        return self.size() == self.buffer_size