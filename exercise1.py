def find_internal_nodes_num(tree):
    ## distinct with set() removing -1
    internal_node_count = max(0, len(set(tree)) - 1)
    return internal_node_count


my_tree = [4, 4, 1, 5, -1, 4, 5]
#my_tree = [9, 5, 5, 5, 3, -1, 2, 3, 1, 1]
count = 0


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []

    def insert(self, data):
        if self.data:
            child = TreeNode(data)
            self.children.append(child)
            child.build_tree()

    def print_tree(self):

        for x in self.children:
            print("child " + str(x.data) + " parent " + str(self.data))
            x.print_tree()

    def build_tree(self):

        global my_tree

        children = [i for i, x in enumerate(my_tree) if x == self.data]

        for child in children:
            self.insert(child)

    def find_internal_nodes_num_with_built_tree(self):
        global count
        parent = False

        for x in self.children:
            parent = True
            x.find_internal_nodes_num_with_built_tree()

        if parent:
            count += 1

        return count


if __name__ == '__main__':

    ## solution by building a tree
    print("## solution by building a tree")
    root_value = my_tree.index(-1)
    root = TreeNode(root_value)
    root.build_tree()
    #root.print_tree()
    print(root.find_internal_nodes_num_with_built_tree())

    
    print("## solution with distinct without building a tree")
    ## solution with distinct without building a tree
    print(find_internal_nodes_num(my_tree))






