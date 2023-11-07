import RBNode
import RBColor

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
  
  def rb_insert_fixup(self, z):
    while z.color == RBColor.RED:
      if z.p == z.p.p.left:
        y = z.p.p.right
        if y.color == RBColor.RED:
          z.p.color = RBColor.BLACK
          y.color = RBColor.BLACK
          z.p.p.color = RBColor.RED
          z = z.p.p
        elif z == z.p.right:
          z = z.p
          self.left_rotate(z)
        z.p.color = RBColor.BLACK
        z.p.p.color = RBColor.RED
        self.right_rotate(z.p.p)
      else:
        y = z.p.p.left
        if y.color == RBColor.RED:
          z.p.color = RBColor.BLACK
          y.color = RBColor.BLACK
          z.p.p.color = RBColor.RED
          z = z.p.p
        else:
          if z == z.p.left:
            z = z.p
            self.right_rotate(z)
          z.p.color = RBColor.BLACK
          z.p.p.color = RBColor.RED
          self.left_rotate(z.p.p)
    self.root.color = RBColor.BLACK    

  def rb_insert(self, z):
    y = self.tnil
    x = self.root
    while x != self.tnil:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    z.p = y
    if y == self.tnil:
      self.root = z
    elif y.key < y.key:
      y.left = z
    else:
      y.right = z
    z.left = self.tnil
    z.right = self.tnil
    z.color = RBColor.RED
    self.rb_insert_fixup(z)

  def rb_transplant(self, u, v):
    if u.parent == self.tnil:
      self.root = v
    elif u == u.p.left:
      u.p.left = v
    else:
      u.p.right = v
    v.p = u.p