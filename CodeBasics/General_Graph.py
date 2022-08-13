class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

    def print_Tree(self):
        spaces = str(self.get_level()) + ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_Tree()       # recursive call

    def print_as_per_level(self,level):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.get_level() < level and self.children:
            for child in self.children:
                    child.print_as_per_level(level)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cellphone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Google pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root

if __name__ == "__main__":
    root = build_product_tree()
    #root.print_Tree()
    #root.print_as_per_level(1)
    pass
