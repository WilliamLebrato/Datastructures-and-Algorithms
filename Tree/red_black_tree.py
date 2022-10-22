"""This is a red black tree structure"""
class Node:
    """
    Each node has 5 attributes
    value - int
    left - a node
    right - a node
    parent - a node
    color - "BLACK"/"RED"
    """
    def __init__(self, value):
        """
        All nodes are created with a value and the color RED.
        Also they have no relations with other nodes.
        """
        self._value = value
        self._left = None
        self._right = None
        self._parent = None
        self._color = "RED"

    def set_left(self, node):
        """
        sets a left child to a node
        """
        self._left = node

    def set_right(self, node):
        """sets a right child to a node"""
        self._right = node

    def set_parent(self, node):
        """sets a parent to a node"""
        self._parent = node

    def children(self, node):
        """sets both children of a node the same node"""
        self._left = node
        self._right = node

    def change_color(self, color):
        """take a string "color" and changes nodes color to it"""
        self._color = color

    def value(self):
        """returns the value of a node"""
        return self._value

    def color(self):
        """returns the color of the node"""
        return self._color

    def right(self):
        """returns the right child of a node"""
        return self._right

    def left(self):
        """returns the left child of a node"""
        return self._left

    def parent(self):
        """returns the parent of a node"""
        return self._parent


class RedBlackTree:
    """A red black tree"""
    def __init__(self):
        """The tree starts empty with a nil node, aslo sets the root to the nil node"""
        self.nil = Node(None)
        self.nil.change_color("BLACK")
        self.root = self.nil

    def subtree_min(self, node):
        """Returns the smallest node in a nodes subtree"""
        while node.left() != self.nil or None:
            node = node.left()
        return node

    def min(self):
        """Uses subtree_min to find the smallest node in the roots subtree"""
        node = self.subtree_min(self.root)
        return node.value()

    def subtree_max(self, node):
        """Returns the largest node in a nodes subtree"""
        while node.right() != self.nil:
            node = node.right()
        return node

    def max(self):
        """Uses subtree_max to finds the largest node in the roots subtree"""
        node = self.subtree_max(self.root)
        return node.value()

    def search(self, value):
        """Returns true if there is a node with a specific value, else returnes false"""
        node = self.root
        while node != self.nil:
            if value == node.value():
                return True
            elif value < node.value():
                node = node.left()
            else:
                node = node.right()
        return False

    def get_node(self, value):
        """If a node exists it returns the node, else it returns False"""
        node = self.root
        while node != self.nil:
            if value == node.value():
                return node
            elif value < node.value():
                node = node.left()
            else:
                node = node.right()
        return False

    def path(self, value):
        """
        If a value exists it returns a list of values from the root to the node
        if the node does not exist it returns false
        """
        if self.search(value) is True:
            path = []
            node = self.root
            while node != self.nil:
                path.append(node.value())
                if value == node.value():
                    return path
                elif value < node.value():
                    node = node.left()
                else:
                    node = node.right()

    def left_rotate(self, node):
        """
        left rotates with node as a pivot
        """
        child = node.right()
        node.set_right(child.left())
        if child.left() != self.nil:
            child.left().set_parent(node)
        child.set_parent(node.parent())
        if node.parent() == self.nil:
            self.root = child
        elif node == node.parent().left():
            node.parent().set_left(child)
        else:
            node.parent().set_right(child)
        child.set_left(node)
        node.set_parent(child)

    def right_rotate(self, node):
        """
        right rotates with node as a pivot
        """
        child = node.left()
        node.set_left(child.right())
        if child.right() != self.nil:
            child.right().set_parent(node)
        child.set_parent(node.parent())
        if node.parent() == self.nil:
            self.root = child
        elif node == node.parent().right():
            node.parent().set_right(child)
        else:
            node.parent().set_left(child)
        child.set_right(node)
        node.set_parent(child)

    def transplant(self, old, new):
        """new takes old place in the tree"""
        if old.parent() == self.nil:
            self.root = new
        elif old == old.parent().left():
            old.parent().set_left(new)
        else:
            old.parent().set_right(new)
        new.set_parent(old.parent())

    def insert(self, value):
        """
        Finds the location where a node should be placed
        """
        node = self.root
        parent = self.nil
        while node != self.nil:
            parent = node
            if value == node.value():
                return
            elif value < node.value():
                node = node.left()
            else:
                node = node.right()
        new_node = Node(value)
        new_node.children(self.nil)
        new_node.set_parent(parent)
        if parent == self.nil:
            self.root = new_node
            self.root.change_color("BLACK")
        else:
            if value < parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)
            self.insert_fixup(new_node)

    def insert_fixup(self, node):
        """
        insertion calls this function, it fixes the tree such as it keeps RBT properties
        """
        while node.parent().color() == "RED":
            if node.parent() == node.parent().parent().right():
                uncle = node.parent().parent().left()
                if uncle.color() == "RED":
                    uncle.change_color("BLACK")
                    node.parent().change_color("BLACK")
                    node.parent().parent().change_color("RED")
                    node = node.parent().parent()
                else:
                    if node == node.parent().left():
                        node = node.parent()
                        self.right_rotate(node)
                    node.parent().change_color("BLACK")
                    node.parent().parent().change_color("RED")
                    self.left_rotate(node.parent().parent())
            else:
                uncle = node.parent().parent().right()
                if uncle.color() == "RED":
                    uncle.change_color("BLACK")
                    node.parent().change_color("BLACK")
                    node.parent().parent().change_color("RED")
                    node = node.parent().parent()
                else:
                    if node == node.parent().right():
                        node = node.parent()
                        self.left_rotate(node)
                    node.parent().change_color("BLACK")
                    node.parent().parent().change_color("RED")
                    self.right_rotate(node.parent().parent())
        self.root.change_color("BLACK")

    def remove(self, value):
        """Removes a node from the tree"""
        node = self.get_node(value)
        if node is not False:
            tracker = node
            tracker_color = tracker.color()
            if node.left() == self.nil:
                child = node.right()
                self.transplant(node, child)
            elif node.right() == self.nil:
                child = node.left()
                self.transplant(node, child)
            else:
                tracker = self.subtree_min(node.right())
                tracker_color = tracker.color()
                child = tracker.right()
                if tracker.parent() == node:
                    child.set_parent(tracker)
                else:
                    self.transplant(tracker, child)
                    tracker.set_right(node.right())
                    tracker.right().set_parent(tracker)
                self.transplant(node, tracker)
                tracker.set_left(node.left())
                tracker.left().set_parent(tracker)
                tracker.change_color(node.color())
            if tracker_color == "BLACK":
                self.remove_fixup(child)

    def remove_fixup(self, node):
        """Is called by remove incase the tree needs fixing"""
        while node != self.root and node.color() == "BLACK":
            if node == node.parent().left():
                sib = node.parent().right()
                if sib.color() == "RED":
                    sib.change_color("BLACK")
                    sib.parent().change_color("RED")
                    self.left_rotate(node.parent())
                    sib = node.parent().right()
                if sib.left().color() == "BLACK" and sib.right().color() == "BLACK":
                    sib.change_color("RED")
                    node = node.parent()
                else:
                    if sib.right().color() == "BLACK":
                        sib.left().change_color("BLACK")
                        sib.change_color("RED")
                        self.right_rotate(sib)
                        sib = node.parent().right()
                    sib.change_color(node.parent().color())
                    node.parent().change_color("BLACK")
                    sib.right().change_color("BLACK")
                    self.left_rotate(node.parent())
                    node = self.root
            else:
                sib = node.parent().left()
                if sib.color() == "RED":
                    sib.change_color("BLACK")
                    sib.parent().change_color("RED")
                    self.right_rotate(node.parent())
                    sib = node.parent().left()
                if sib.left().color() == "BLACK" and sib.right().color() == "BLACK":
                    sib.change_color("RED")
                    node = node.parent()
                else:
                    if sib.left().color() == "BLACK":
                        sib.right().change_color("BLACK")
                        sib.change_color("RED")
                        self.left_rotate(sib)
                        sib = node.parent().left()
                    sib.change_color(node.parent().color())
                    node.parent().change_color("BLACK")
                    sib.left().change_color("BLACK")
                    self.right_rotate(node.parent())
                    node = self.root
        node.change_color("BLACK")

    @staticmethod
    def convert(nodes):
        """Transformes each node in a list to a list of values"""
        for i in range(len(nodes)):
            data_dict = nodes[i].__dict__
            value = data_dict["_value"]
            color = data_dict["_color"]
            left = data_dict["_left"]
            right = data_dict["_right"]
            data = [value, color, left.value(), right.value()]
            nodes[i] = data
        return nodes


    def bfs(self):
        """Creates a list of the tree from top to"""
        bfs_list = []
        if self.root != self.nil:
            nodes = [self.root]
            while nodes != []:
                children = []
                for node in nodes:
                    if node.left() != self.nil:
                        children.append(node.left())
                    if node.right() != self.nil:
                        children.append(node.right())
                bfs_list.extend(nodes)
                nodes = children
            bfs_list = self.convert(bfs_list)
        return bfs_list
