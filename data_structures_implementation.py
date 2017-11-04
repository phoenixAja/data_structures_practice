
# coding: utf-8

# In[1]:

#from test import testEqual
from pythonds.basic.stack import Stack, Queue
import unittest

# implement a stack in python
class Stack:
    
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def get_length(self):
        length = len(self.stack)
        return length
        
    def push(self, val):
        self.stack.append(val)
        
    def pop(self, val):
        last_val = self.stack.pop()
        return last_val


# In[13]:


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
        stack.push(char)
        
    new_str = ''
    
    while not stack.isEmpty():
        new_str += stack.pop()
        
    return new_str    


def balanced_parentheses(paren_str):
    # problem involving applications of stack
    
    opening = Stack()
    
    for i in paren_str:
        if i in ("(", "{", "["):
            opening.push(i)
        
        else:
            if not opening.isEmpty():
                if   i == ")" and opening.peek() == "(":
                    opening.pop()
                elif i == "}" and opening.peek() == "{":
                    opening.pop()
                elif i == "]" and opening.peek() == "[":
                    opening.pop()
                else:
                    return False
                
            else:
                return False

    return True        
            


# In[19]:

balanced_parentheses('[([])]]{}]{]}')


# In[12]:

s = Stack()
s.push(2)
s.push(3)
s.peek()


# In[50]:

class Queue_pal:
    
    def __init__(self):
        self.items = []
        
    def add(self, val):
        self.items.insert(0, val)
    
    def get(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def get_length(self):
        return len(self.items)
    

def hot_potato(names_lst, num):
    # returns the last person surviving in the queue
    
    names = Queue_pal()
    
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
            print("safe", names.get())
            turns = 1
    
    # get the survivor off of the queue
    return names.get()
        
    
    
    
    


# In[51]:

names = ['bryan', 'louis', 'cynthia', 'randall', 'joshua', 'heidi']
hot_potato(names, 4)


# In[ ]:



