# implement a stack in python
class Stack:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def get_length(self):
        length = len(self.items)
        return length
        
    def add(self, val):
        self.items.append(val)
        
    def get(self):
        last_val = self.items.pop()
        return last_val

    def peek(self):
        return self.items[len(self.items) - 1]


class Queue(Stack):
    # inherit from stack since mostly similar  
    def add(self, val):
        # more efficient to use stack O(1) instead of O(n)
        self.items.insert(0, val)
    