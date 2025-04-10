class bookNode:  # Binary Search Tree (BST)
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.left = None
        self.right = None


class BookLibrary:
    def __init__(self):
        self.root = None  # The root of the tree, initially empty

    # insert fucntion
    def _insert(self, node, name, author, year):
        if node is None:
            return bookNode(name, author, year)
        if name > node.name:
            node.right = self._insert(node.right, name, author, year)
        elif name < node.name:
            node.left = self._insert(node.left, name, author, year)
        return node

    # function use to insertBook ( this function use _insert function)
    def insert(self, name, author, year):
        self.root = self._insert(self.root, name, author, year)

    # search function
    def _search(self, node, name):
        if node is None or node.name == name:
            return node  # If the node is found or the node is empty (not found)
        if name > node.name:
            return self._search(node.right, name)
        else:
            return self._search(node.left, name)

    # function use to search ( this function use _search function)
    def search(self, name):
        return self._search(self.root, name)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete function
    def _delete(self, node, name):
        if node is None:
            return node
        if name > node.name:
            node.right = self._delete(node.right, name)
        elif name < node.name:
            node.left = self._delete(node.left, name)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.name = min_larger_node.name
            node.author = min_larger_node.author
            node.year = min_larger_node.year
            node.right = self._delete(node.right, min_larger_node.name)
        return node

    def delete(self, name):
        self.root = self._delete(self.root, name)

    # Search function
    def _inorder(self, node, books):
        if node:
            self._inorder(node.left, books)
            books.append(
                f"Book: {node.name}, Author: {node.author}, Year: {node.year}\n"
            )
            self._inorder(node.right, books)

    # Function to get books as a string
    def display_books(self):
        books = []
        self._inorder(self.root, books)
        return "".join(books)
