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