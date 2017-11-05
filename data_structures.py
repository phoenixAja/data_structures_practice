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


class Dequeue(Queue):
    # a mixture of both Queues and stack, can retrieve and items to 
    # both front and back of a dequeue

    def add_to_front(self, val):
        super(Dequeue, self).add(val)

    def add_to_end(self, val):
        # call to the stack add method
        super(Queue, self).add(val)

    def get_from_end(self):
        # use queue get() method
        super(Dequeue, self).get()

    def get_from_front(self, val):
        #create new method for this
        return self.items.pop(0)

    def peek_front(self):
        # create new method
        return self.items[0]

    def peek_end(self):
        super(Dequeue, self).peek()    
    