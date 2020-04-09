import copy

class Tree():
    def __init__(self, value, children=[]):
        self.__value = value
        self.__children = copy.deepcopy(children)

    @property
    def value(self):
        return self.__value

    @property
    def children(self):
        return copy.deepcopy(self.__children)

    def addChild(self, tree):
        self.__children.append(tree)

    @property
    def size(self):
        result = 1
        for child in self.__children:
            result += child.size
        return result

    def __getitem__(self, index):
        return self.__children[index]

    def __str__(self):
        def _str(tree, depth):
            result = '[{}]\n'.format(tree.__value)
            for child in tree.children:
                result += '{}|--{}'.format('    ' * depth, _str(child, depth + 1))
            return result
        return _str(self, 0)

def addBranch(root, n):
    if n == 1:
        root.addChild(Tree(n))
        return root
    root.addChild(Tree(n))
    return addBranch(root, n-1)
    
def addLevel(root, depth, branches):
    current_root = Tree(None)
    if depth == 1 :
        return root
    for child in current_root :
        addBranch(child, root)
    return root

def test(depth, root, children):
    for child in children:
        print(child)
        if depth == 1:
            root.addChild(Tree(child))
            return root
        root.addChild(Tree(child))
    new_root = children
    return test(depth-1, new_root, children)

t1 = Tree('ROOT')
t2 = [1, 2, 3, 4]

#print(test(3, t1, t2))
t3 = Tree(1, 2, 3, 4)
print(t1.addChild(t3))