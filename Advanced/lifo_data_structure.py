"""
L.I.F.O.(Last in First Out) are one of the fundemental data structures in Computer Science. 
As the name implies, the last item is also the first one to go."""

class LifoStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) -1
        return self.items[last]
        
    def size(self):
        return len(self.items)


