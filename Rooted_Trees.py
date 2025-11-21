class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class RootedTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def _search(self, node, value):
        if node.data == value:
            return node
        for child in node.children:
            found = self._search(child, value)
            if found:
                return found
        return None

    # Access
    def access(self, value):
        """Return the node with the given value, or None."""
        return self._search(self.root, value)

    # Insertion
    def insert(self, parent_value, new_value):
        """Insert a new node as a child of a node with parent_value."""
        parent_node = self._search(self.root, parent_value)
        if parent_node is None:
            raise ValueError(f"Parent '{parent_value}' not found.")

        parent_node.children.append(TreeNode(new_value))

    # Update
    def update(self, old_value, new_value):
        """Update the data of an existing node."""
        node = self._search(self.root, old_value)
        if node is None:
            raise ValueError(f"Node '{old_value}' not found.")

        node.data = new_value

    # Delete
    def delete(self, value):
        if self.root.data == value:
            raise ValueError("Cannot delete the root node.")

        # BFS to find the parent
        queue = [self.root]

        while queue:
            current = queue.pop(0)

            for child in current.children:
                if child.data == value:
                    current.children.remove(child)
                    return True

            queue.extend(current.children)

        return False  # not found

    # Display (tree structure)
    def display(self, node=None, level=0):
        if node is None:
            node = self.root

        print(" " * (level * 4) + str(node.data))
        for child in node.children:
            self.display(child, level + 1)

    # Traversals (optional)
    def dfs(self, node=None):
        if node is None:
            node = self.root
        print(node.data)
        for child in node.children:
            self.dfs(child)

    def bfs(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.data)
            queue.extend(current.children)


# Example Usage
if __name__ == "__main__":
    tree = RootedTree("A")

    tree.insert("A", "B")
    tree.insert("A", "C")
    tree.insert("B", "D")
    tree.insert("B", "E")

    print("Initial Tree:")
    tree.display()

    print("\nUpdate 'C' to 'Z':")
    tree.update("C", "Z")
    tree.display()

    print("\nDelete Node 'B':")
    tree.delete("B")
    tree.display()

    print("\nAccess Node 'Z':")
    node = tree.access("Z")
    print("Found:", node.data if node else "Not found")
