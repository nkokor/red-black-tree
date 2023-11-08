from classes.RBNode import RBNode
from classes.RBTree import RBTree

rb_tree = RBTree()

def run_app():
  running = True
  while running:
    print("1 - Insert new node")
    print("2 - Inorder traversal")
    print("3 - Delete node")
    print("4 - Exit")
    print("Input option number: ")
    option = int(input())
    if option == 4:
      running = False
    else:
      if option == 1:
        print("Input key value: ")
        key = int(input())
        new_node = RBNode(key)
        rb_tree.rb_insert(new_node)
      elif option == 2:
        print(rb_tree.get_inorder(rb_tree.root))
      elif option == 3:
        print("Input key to delete: ")
        key = int(input())
        node = rb_tree.get_node_with_key(key)
        if node != None:
          rb_tree.rb_delete(node)
        else:
          print("No node with such value found in tree!")
      else:
        print("Wrong input!")

run_app()