import re
import itertools
from data_structures import Stack, Queue, Dequeue
from custom_exceptions import WrongTypeException

def revstring(str):
    # without stack
    str_lst = list(str)
    new_str = ''
    
    while len(str_lst) > 0:
        new_str += str_lst.pop()
        
    return new_str
    
def revstringstack(str):
    # with stack implemented
    stack = Stack()
    
    for char in str:
        stack.add(char)
        
    new_str = ''
    
    while not stack.isEmpty():
        new_str += stack.get()
        
    return new_str    


def balanced_parentheses(paren_str):
    """problem involving applications of stack"""

    # filter out all values besides brackets
    matches = re.finditer(r'[(){}[\]]+', paren_str)
    parsed_iter = itertools.chain.from_iterable(
                            result.group() 
                            for result in matches)
    
    opening = Stack()
    
    for i in parsed_iter:
        if i in ("(", "{", "["):
            opening.add(i)
        
        else:
            if not opening.isEmpty():
                if   i == ")" and opening.peek() == "(":
                    opening.get()
                elif i == "}" and opening.peek() == "{":
                    opening.get()
                elif i == "]" and opening.peek() == "[":
                    opening.get()
                else:
                    return False
                
            else:
                return False

    return True  


def hot_potato(names_lst, num):
    """     
     queue data structure implementation
     returns the last person surviving in the queue
     """
    
    names = Queue()
    
    for i in names_lst:
        # add the names to the queue
        names.add(i)
    
    turns = 1
    while names.get_length() > 1:
        
        if turns < num:
            # get and return items to queue
            potato = names.get()
            names.add(potato)
            turns += 1
            
        else:
            # when turns == num remove item
            names.get()
            turns = 1
    
    # get the survivor off of the queue
    return names.get()       


def palindrome_check(input):
    """
    implementation of Dequeue, will check if string is palindrome
    """
    if type(input) != str:
        raise WrongTypeException("input item needs to be of type str")

    dequeue = Dequeue()

    for i in input:  
        dequeue.add_to_end(i) # use add_to_end O(1) vs. O(n)

    is_palindrome = True

    while is_palindrome == True and dequeue.get_length() > 1:
        if dequeue.get_from_end() != dequeue.get_from_front():
            is_palindrome = False

    return is_palindrome
















