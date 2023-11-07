import RBColor

class RBNode():

  def __init__(self, key):
    self.p = None
    self.left = None
    self.right = None
    self.key = key
    if key == None:
      self.color = RBColor.BLACK
    else:
      self.color = RBColor.RED

  def print_node(self):
    if self.key == None:
      print(f"T.nil")
    else:
      if self.p.key == None:
        print(f"ROOT NODE, key: ${self.key} color: ${self.color} parent: T.nil left child: ${self.left.key} right child: ${self.right.key}")
      else:
        print(f"key: ${self.key} color: ${self.color} parent: ${self.p.key} left child: ${self.left.key} right child: ${self.right.key}")