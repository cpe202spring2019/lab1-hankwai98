import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""

        self.assertEqual(max_list_iter([7,4,9,5]),9)        # Postive Integer List
        self.assertEqual(max_list_iter([-6,-8,-10,-3,0]),0) # Negative Integer List
        self.assertEqual(max_list_iter([1]),1)              # Single Element List
        self.assertEqual(max_list_iter([]),None)            # Empty List
        tlist = None                                        # None Object
        with self.assertRaises(ValueError):  
            max_list_iter(tlist)
 
    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])          # Positive Integer List     
        self.assertEqual(reverse_rec([-2,-3,-4]),[-4,-3,-2])    # Negative Integer List
        self.assertEqual(reverse_rec([7]),[7])                  # Single Element List
        self.assertEqual(reverse_rec([]),[])                    # Empty List
        tlist = None                                            # None Object
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
        
    def test_bin_search(self):
        list_val = None                                         
        with self.assertRaises(ValueError):                     # None Object Returns ValueError
            bin_search(4, 1, 7, list_val)

        list_val =[]                                                
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), None ) # Empty List Returns None

        list_val =[0,1,2,3,4,7,8,9,10]                              
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4 )    # Mid Index is Target

        list_val =[0,1,2,3,4,7,8,9,10]                              
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 1 )    # Mid Index above Target

        list_val =[0,1,2,3,4,7,8,9,10]                              
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(9, low, high, list_val), 7 )    # Mid Index below Target

if __name__ == "__main__":
        unittest.main()

    
