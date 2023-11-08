from RBColor import RBColor

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

  def to_string(self):
    if self.key == None:
      return "T.nil\n"
    else:
      left_child = self.left.key
      right_child = self.right.key
      if left_child == None:
        left_child = "T.nil"
      if right_child == None:
        right_child = "T.nil"
      if self.p.key == None:
        return f"ROOT NODE, key: {self.key}, color: {self.color.value}, parent: T.nil left child: {left_child}, right child: {right_child}\n"
      else:
        return f"key: {self.key}, color: {self.color.value}, parent: {self.p.key}, left child: {left_child}, right child: {right_child}\n"