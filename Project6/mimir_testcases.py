import unittest
from PriorityHeap import PriorityHeap, Node, heap_sort, current_medians


class MimirTests(unittest.TestCase):

   l = current_medians([2,14,6,8,10,15,12])
   print(l)
if __name__ == '__main__':
    unittest.main()
