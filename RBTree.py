import RBNode

class RBTree():

  def __init__(self):
    self.tnil = RBNode(None)
    self.root = self.TNIL
    self.n = 0

  def left_rotate(self, x):
    y = x.right
    x.right = y.left
    if y.left != self.tnil:
      y.left.p = x
    y.p = x.p
    if x.p == self.tnil:
      self.root = y
    elif x == x.p.left:
      x.p.left = y
    else:
      x.p.right = y
    y.left = x
    x.p = y

  def right_rotate(self, x):
    y = x.left
    x.left = y.right
    if y.right != self.tnil:
      y.right.p = x
    y.p = x.p
    if x.p == self.tnil:
      self.root = y
    elif x == x.p.left:
      x.p.left = y
    else:
      x.p.right = y
    y.right = x
    x.p = y
