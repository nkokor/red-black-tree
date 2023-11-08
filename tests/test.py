import unittest
from classes.RBTree import RBTree
from classes.RBNode import RBNode

class RBTreeTest(unittest.TestCase):
        
  def test_1(self):
    tree = RBTree()
    keys = [6, 11, 10, 2, 9, 7, 5, 13, 22, 27, 36, 12, 31]
    for key in keys:
      node = RBNode(key)
      tree.rb_insert(node)
    expected_result = "2 black 5 red 6 black 7 red 9 black 10 black 11 black 12 red 13 black 22 black 27 red 31 red 36 black "
    actual_result = tree.get_inorder(tree.root)
    print(expected_result)
    print(actual_result)
    self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()