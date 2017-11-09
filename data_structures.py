from custom_exceptions import EmptyItemsError, MethodNotAvailable, ItemNotInList


class Stack:
    
    def __init__(self):
        self.items = []
        
    def check_items(self):
        if self.isEmpty():
            raise EmptyItemsError("No Items in {struct}".format(struct=self.__class__.__name__))   
        else:
            pass
        
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
        self.check_items()
        last_val = self.items.pop()
        return last_val

    def peek(self):
        self.check_items()
        return self.items[len(self.items) - 1]


class Queue(Stack):
    """inherit from stack since mostly similar  """

    def add(self, val):
        self.items.insert(0, val) # more efficient to use stack O(1) instead of O(n)


class StructureMixin(Queue):
    """     
     I am going to rename these methods in Dequeu class for less 
     ambiguous naming, and potentially in other data structures I 
     will need to do something similar, therefore a mixin seems like
     the best approach
     """

    def add(self, val):
        pass
    
    def get(self, val):
        pass
    
    def peek(self):
        pass


class Dequeue(StructureMixin, Queue):
    """    
    a mixture of both Queues and stack, can retrieve and items to 
    both front and back of a dequeue
    """

    def add_to_front(self, val):
        #super(Dequeue, self).add(val)
        Queue.add(self, val)

    def add_to_end(self, val):
        # call to the stack add method
        super(Queue, self).add(val)

    def get_from_end(self):
        # use queue get() method
        return super(Queue, self).get()

    def get_from_front(self):
        #create new method for this
        self.check_items()
        return self.items.pop(0)

    def peek_front(self):
        # create new method
        self.check_items()
        return self.items[0]

    def peek_end(self):
        #super(Dequeue, self).peek()  
        return super(Queue, self).peek()
    

class Node:
    """
    used to create parts of linked list
    not mine, taken from Problem Solving with Algorythms and Data Structures Using Python 
    by Bradley N. Miller and David L. Ranum
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data, ):
        self.data = new_data

    def set_next(self, new_next_data):
        self.next = new_next_data    



class List:
    """linked list"""

    def __init__(self):
        # store nodes in list
        self.head = None
    
    @staticmethod
    def check_items(self):
        if self.head == None:
            raise EmptyItemsError("No Items in {struct}".format(struct=self.__class__.__name__))   
        else:
            pass
        
    def add(self, val):
        # assume the item is not in the list?
        new = Node(val)
        new.set_next(self.head)
        self.head = new    

    def size(self):
        """returns the size of the list"""
        size = 0
        initial = self.head
        while initial != None:
            size += 1
            print(initial.get_data())
            initial = initial.get_next()
        return size
    
    def search(self, val):
        """returns boolean if value is in the list"""
        self.check_items()
        initial = self.head
        while initial != None:
            if initial.get_data() == val:
                return True
            else:
                initial = initial.get_next()
                
        return False
    
    # def remove(self, val):
    #     """remove value from list"""
    #     self.check_items()
    #     initial = self.head
    #     while initial != None:
    #         if initial.get_data() == val:
                

    def peek(self):
        raise MethodNotAvailable




