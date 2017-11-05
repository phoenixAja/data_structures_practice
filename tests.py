import unittest


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


class TestDataStructureImplementations(unittest.TestCase):
    
    # test stack implementation of balanced parantheses
    def test_balanced_paranthesis(self):
        # basic case
        self.assertEqual(balanced_parentheses('[([])]]{}]{]}'), False)
        self.assertEqual(balanced_parentheses('(({{[]}}))'), True)
                         
        # test in case empty
        self.assertEqual(balanced_parentheses(''), True)
        
        # test with other characters
        self.assertEqual(balanced_parentheses('A{VB[12k(())]}'), True)
        self.assertEqual(balanced_parentheses('th7&{}}}['), False)

    # test queue implementation of hot potato 
    def test_hot_potato(self):
        names = ['bryan', 'louis', 'cynthia', 'randall']
        self.assertEqual(hot_potato(names, 4), 'louis')
        

        
        


