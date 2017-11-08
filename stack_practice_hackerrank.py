# You have an empty sequence, and you will be given  queries. Each query is one of these three types:
# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.

# Input Format:
# The first line of input contains an integer, . The next  lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

# Constraints: 
#  1 <= N <= 10^5
#  1 <= x <= 10^9
#  1 <= type <= 3
 
# Output Format:
# For each type  query, print the maximum element in the stack on a new line.
# Sample Input:
# 10
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3
# Sample Output:
# 26
# 91
import os
import sys
#from pythonds.basic.stack import Stack


"""adding in some custom errors"""
class NotValidType(Exception):
    """raised if query not of type 1,2,3"""

class ItemOutOfBounds(Exception):
    """raised if any input value is too large"""

class NotAFile(Exception):
    """raised if user did not enter an actual file as input"""

class EmptyItemsError(Exception):
    """
    Raised when items is empty
	used for peek() and get() variations
    """
class WrongTypeException(Exception):
    """
	Raised when wrong type is encountered for data
	structure implementation
	"""
class MethodNotAvailable(Exception):
    """
	Raised when user tries to use method that is 
	not available to current structure
	"""
class ItemNotInList(Exception):
    """
	Raised when user tries to retrieve item that doesn't exist (for list)
	"""


class Stack:
    
    def __init__(self):
        self.items = []
        self.size = 0
        self.times_popped = 0
        self.largest_val = 0
        self.largest_val_pos = 0
        
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
    
    def size(self):
        length = len(self.items)
        return length
        
    def push(self, val):
        self.size += 1
        if val > self.largest_val:
            self.largest_val = largest_val
            self.largest_val_pos = self.size
            
        self.items.append(val)
        
    def pop(self):
        self.check_items()
        self.times_popped += 1
        last_val = self.items.pop()
        return last_val

    def peek(self):
        self.check_items()
        return self.items[len(self.items) - 1]

    def 


def query_to_stack(query_string):
 
    query_type = int(query_string[0])

    if query_type == 1:
        query, input = tuple(query_string.split(" "))
        stack.push(int(input))
        query_1_count += 1
            
    elif query_type == 2:
        stack.pop()
        query_2_count +=1

    elif query_type ==3:
        """filter stack and return highest value"""
        temp_stack = Stack() # for storing values as we traverse through the stack
        highest_val = stack.peek() # set the highest val as that on top of the stack

        while not stack.isEmpty(): # go through eac value in the stack
            top_val = stack.pop() # get top value from the stack
            if top_val > highest_val:  
                highest_val = top_val # set new highest_val to whatever was at the top pf the stack
            temp_stack.push(top_val) # push value to temp_stack to preserve order

        while not temp_stack.isEmpty(): # go through temp_stack until empty and add to stack
            stack.push(temp_stack.pop())
         
        yield highest_val

    else:
        raise NotValidType("some queries in file are not of type 1,2,3")


def track_highest_val(highest):
    values_added_since = 0
    values_removed_since = 0
    current_highest = 0
    
    while True:




def track_since_last_2(times):
    """keeps track of whenever the last 2 was called"""


if __name__ == "__main__":

    stack = Stack()
    highest_values_stack = Stack()
    query_input = sys.stdin

    true_length = 0
    specified_length = int(next(query_input))

    #if specified_length in range(0, 10**5):
    while true_length < specified_length:
        for q in query_input:
            true_length += 1
            val = next(query_to_stack(q))
            if val != None:
                sys.stdout.write(str(val) + "\n")

    # else: 
    #     raise ItemOutOfBounds("wrong expected number of inputs or input list is too long")


