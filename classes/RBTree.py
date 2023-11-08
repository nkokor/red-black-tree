from classes.RBColor import RBColor
from classes.RBNode import RBNode

class RBTree():

  def __init__(self):
    self.tnil = RBNode(None)
    self.root = self.tnil
    self.n = 0

  def get_node_with_key(self, key):
    current = self.root
    while current != self.tnil:
      if current.key == key:
        return current
      else:
        if key < current.key:
          current = current.left
        else:
          current = current.right
    return None

  def left_rotate(self, x: RBNode):
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

  def right_rotate(self, x: RBNode):
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
  
  def rb_insert_fixup(self, z: RBNode):
    while z.p.color == RBColor.RED:
      if z.p == z.p.p.left:
        y = z.p.p.right
        if y.color == RBColor.RED:
          z.p.color = RBColor.BLACK
          y.color = RBColor.BLACK
          z.p.p.color = RBColor.RED
          z = z.p.p
        else:
          if z == z.p.right:
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

  def rb_insert(self, z: RBNode):
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
    elif z.key < y.key:
      y.left = z
    else:
      y.right = z
    z.left = self.tnil
    z.right = self.tnil
    z.color = RBColor.RED
    self.rb_insert_fixup(z)

  def rb_transplant(self, u: RBNode, v: RBNode):
    if u.p == self.tnil:
      self.root = v
    elif u == u.p.left:
      u.p.left = v
    else:
      u.p.right = v
    v.p = u.p

  def tree_minimum(self, x: RBNode):
    while x.left != self.tnil:
      x = x.left
    return x

  def rb_delete_fixup(self, x: RBNode):
    while x != self.root and x.color == RBColor.BLACK:
      if x == x.p.left:
        w = x.p.right
        if w.color == RBColor.RED:
          w.color = RBColor.BLACK
          x.p.color = RBColor.RED
          self.left_rotate(x.p)
          w = x.p.right
        if w.left.color == RBColor.BLACK and w.right.color == RBColor.BLACK:
          w.color = RBColor.RED
          x = x.p
        else:
          if w.right.color == RBColor.BLACK:
            w.left.color = RBColor.BLACK
            w.color = RBColor.RED
            self.right_rotate(w)
            w = x.p.right
          w.color = x.p.color
          x.p.color = RBColor.BLACK
          w.right.color = RBColor.BLACK
          self.left_rotate(x.p)
          x = self.root
      else:
        w = x.p.left
        if w.color == RBColor.RED:
          w.color = RBColor.BLACK
          x.p.color = RBColor.RED
          self.right_rotate(x.p)
          w = x.p.left
        if w.right.color == RBColor.BLACK and w.left.color == RBColor.BLACK:
          w.color = RBColor.RED
          x = x.p
        else:
          if w.left.color == RBColor.BLACK:
            w.right.color = RBColor.BLACK
            w.color = RBColor.RED
            self.left_rotate(w)
            w = x.p.left
          w.color = x.p.color
          x.p.color = RBColor.BLACK
          w.left.color = RBColor.BLACK
          self.right_rotate(x.p)
          x = self.root
    x.color = RBColor.BLACK

  def rb_delete(self, z: RBNode):
    y = z
    y_original_color = y.color
    if z.left == self.tnil:
      x = z.right
      self.rb_transplant(z, z.right)
    elif z.right == self.tnil:
      x = z.left
      self.rb_transplant(z, z.left)
    else:
      y = self.tree_minimum(z.right)
      y_original_color = y.color
      x = y.right
      if y != z.right:
        self.rb_transplant(y, y.right)
        y.right = z.right
        y.right.p = y
      else: 
        x.p = y
      self.rb_transplant(z, y)
      y.left = z.left
      y.left.p = y
      y.color = z.color
    if y_original_color == RBColor.BLACK:
      self.rb_delete_fixup(x)
    
  def rb_inorder_traversal(self, x: RBNode):
    if x.key != None:
      self.rb_inorder_traversal(x.left)
      print(x.to_string())
      self.rb_inorder_traversal(x.right)

  def get_inorder(self, x: RBNode, inorder = ""):
    if x.key != None:
      inorder = self.get_inorder(x.left, inorder)
      inorder += str(x.key) + " " + x.color.value + " "
      inorder = self.get_inorder(x.right, inorder)
    return inorder