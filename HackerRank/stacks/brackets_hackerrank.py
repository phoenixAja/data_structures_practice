#!/bin/python3

import sys
import itertools

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


def isBalanced(s):
    """problem involving applications of stack"""

    # filter out all values besides brackets

    parsed_iter = (char for char in s)
    
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
                    return "NO"
                
            else:
                return "NO"
            
    if opening.isEmpty():        
        return "YES"
    else:
        # check if opening bracket is on top of stack
        return "NO"

        

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)