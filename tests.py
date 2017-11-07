import unittest
from data_structures import Stack, Queue, Dequeue
import data_structures_implemented as dsi
from custom_exceptions import EmptyItemsError, WrongTypeException, MethodNotAvailable, ItemNotInList


class TestStack(unittest.TestCase):
    
    @staticmethod
    def add_to_structure(self, items):
        for i in items:
            self.structure.add(i)
        
    def setUp(self):
        self.structure = Stack() 
    
    def test_structure_isEmpty(self):
        self.assertEqual(self.structure.isEmpty(), True)
        
        self.add_to_structure(self, range(3))    
        self.assertEqual(self.structure.isEmpty(), False)
             
    def test_structure_peek(self):
        
        structure = self.add_to_structure(self, iter(['people', 'potatoes', 'pansies']))
        self.assertEqual(self.structure.peek(), 'pansies')
            
    def test_structure_get_length(self):
        structure = self.add_to_structure(self, range(5))
        self.assertEqual(self.structure.get_length(), 5)
        
    def test_structure_get(self):
        structure = self.add_to_structure(self, range(3))
        
        # test that first in are first out
        for i in reversed(range(3)):
            self.assertEqual(self.structure.get(), i)
            
    def test_empty_items(self):
        # for when get, or peek is called on empty structure
        self.assertRaises(EmptyItemsError, lambda: self.structure.get())
        self.assertRaises(EmptyItemsError, lambda: self.structure.peek())


class TestQueue(TestStack):
    
    # inherit from testStack since similar tests will be run with Queue
    def setUp(self):
        self.structure = Queue()
    
    def test_structure_peek(self):
        structure = self.add_to_structure(self, iter(['people', 'potatoes', 'pansies']))
        # first word to the queue appears with peak
        self.assertEqual(self.structure.peek(), 'people')
        
    def test_structure_get(self):
        structure = self.add_to_structure(self, range(3))
        
        # test that last in are first out
        for i in range(3):
            self.assertEqual(self.structure.get(), i)

    

class TestDequeue(unittest.TestCase):
        
    def setUp(self):
        self.structure = Dequeue()
        
    @staticmethod
    def add_to_structure_end(self, items):
        for i in items:
            self.structure.add_to_end(i)
        
    @staticmethod
    def add_to_structure_front(self, items):
        for i in items:
            self.structure.add_to_front(i)
            
    def test_structure_front_peek(self):
        self.add_to_structure_front(self, iter(['people', 'places', 'things']))
        self.assertEqual(self.structure.peek_front(), 'things')
        
    def test_structure_end_peek(self):
        self.add_to_structure_end(self, iter([1,2,3,4,5]))
        self.assertEqual(self.structure.peek_end(), 5)
        
    def test_structure_isEmpty(self):
        self.assertEqual(self.structure.isEmpty(), True)
        self.add_to_structure_front(self, range(3))    
        self.assertEqual(self.structure.isEmpty(), False)
        
    def test_structure_get_length(self):
        self.add_to_structure_front(self, range(5))
        self.assertEqual(self.structure.get_length(), 5)
        
    def test_structure_get_front(self):
        self.add_to_structure_front(self, range(4))
        self.assertEqual(self.structure.get_from_front(), 3)
        
    def test_structure_get_end(self):
        self.add_to_structure_end(self, range(4))
        self.assertEqual(self.structure.get_from_end(), 3)
        
    def test_empty_items(self):
        # for when get, or peek is called on empty structure
        self.assertRaises(EmptyItemsError, lambda: self.structure.get_from_front())
        self.assertRaises(EmptyItemsError, lambda: self.structure.get_from_end())
        self.assertRaises(EmptyItemsError, lambda: self.structure.peek_front())
        self.assertRaises(EmptyItemsError, lambda: self.structure.peek_end())



class TestUnorderedList(TestStack):
    """inherit from TestStack since most methods there can get reused"""

    def setUp(self):
        self.structure = UnorderedList()
 
    def test_structure_peek(self):
        self.assertRaises(MethodNotAvailable, lambda: self.structure.peek())
            
    def test_structure_get_length(self):
        structure = self.add_to_structure(self, range(5))
        self.assertEqual(self.structure.get_length(), 5)
        
    def test_structure_get(self):
        self.assertRaises(MethodNotAvailable, lambda: self.structure.get())
            
    def test_empty_items(self):
        # for when attempt to retrieve is called on empty list
        self.assertRaises(EmptyItemsError, lambda: self.structure.pop())
        self.assertRaises(EmptyItemsError, lambda: self.structure.remove())
        self.assertRaises(EmptyItemsError, lambda: self.structure.insert(3,"fire"))
        # when item not in list

    def test_remove_item(self):
        self.add_to_structure(self, range(3))
        self.structure.remove(2)
        self.assertEqual(self.structure.items, [0, 1])
        self.assertRaises(ItemNotInList, lambda: self.structure.remove(6))

    def test_search(self):
        self.add_to_structure(self, iter('Thomas', 'Harriet', 'George'))
        self.assertEqual(self.structure.search('Thomas'), True)
        self.assertEqual(self.structure.search('Paul'), False)    

    def test_index(self):
        self.add_to_structure(self, iter(['dalmation', 'spaniel', 'greyhound', 'huskey']))
        self.assertEqual(self.structure.index('spaniel'), 1)
        self.assertEqual(self.structure.index('huskey'), 3)
        self.assertRaises(ItemNotInList, lambda: self.structure.index('chihuahua'))

    def test_insert(self):
        self.add_to_structure(self, range(3))
        self.assertEqual(self.structure.insert(1,'alchemy'), [0, 'alchemy', 1, 2])

    def test_get_pos(self):
        self.assertRaises(ItemNotInList, lambda: self.structure.pop(4))
        self.add_to_structure(self, iter(['A', 4, None, 'Mix']))
        self.assertEqual(self.structure.get(1), 4)



class TestDataStructureImplementations(unittest.TestCase):
    
    # test stack implementation of balanced parantheses
    def test_balanced_paranthesis(self):
        # basic case
        self.assertEqual(dsi.balanced_parentheses('[([])]]{}]{]}'), False)
        self.assertEqual(dsi.balanced_parentheses('(({{[]}}))'), True)
                         
        # test in case empty
        self.assertEqual(dsi.balanced_parentheses(''), True)
        
        # test with other characters
        self.assertEqual(dsi.balanced_parentheses('A{VB[12k(())]}'), True)
        self.assertEqual(dsi.balanced_parentheses('th7&{}}}['), False)

    # test queue implementation of hot potato 
    def test_hot_potato(self):
        names = ['bryan', 'louis', 'cynthia', 'randall']
        self.assertEqual(dsi.hot_potato(names, 4), 'louis')


    def test_palindrome_checked(self):
    	palindrome = "racecar"
    	not_palindrome = "coffee"
    	not_char = 3
    	empty = ""

    	self.assertEqual(dsi.palindrome_check(palindrome), True)
    	self.assertEqual(dsi.palindrome_check(empty), True)
    	self.assertEqual(dsi.palindrome_check(not_palindrome), False)
    	self.assertRaises(WrongTypeException, lambda: dsi.palindrome_check(not_char))

        


if __name__ == '__main__':
    unittest.main()        
        


