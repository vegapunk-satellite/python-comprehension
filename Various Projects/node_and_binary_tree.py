
class Node:
    def __init__(self, book_id, book, left_node, right_node):
        self.book_id = book_id
        self.book = book
        self.left_node = left_node
        self.left_node = left_node

class BinaryTree:
    def __init__(self, book_id, book):
        self.root = Node(book_id, book, None, None)

    def add_book(self, book_id, book):
        new_node = Node(book_id, book, None, None)
        current_node: Node = self.root
        while current_node is not None:
            if current_node.book_id < book_id:
                current_parent = current_node
                add_to_right = True
                current_node = current_node.right_node
            elif book_id < current_node.book_id:
                current_parent = current_node
                add_to_right = False
                current_node = current_node.left_node
            else:
                raise RuntimeError("You already have this book")
        if add_to_right:
            current_parent.right_node = new_node
        else:
            current_parent.left_node = new_node


    def search_book(self, book_id):
        current_node: Node = self.root
        while current_node is not None:
            if current_node.book_id < book_id:
                current_node = current_node.right_node
            elif book_id < current_node.book_id:
                current_node = current_node.left_node
            else:
                return current_node.book
        return None

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, first_book_id, first_book):
        self.binary_tree = BinaryTree(first_book_id, first_book)

    def add_book(self, book_id: str, book: Book):
        self.binary_tree.add_book(book_id, book)

    def search_book(self, book_id: str) -> Book:
        return self.binary_tree.search_book(book_id)


#Link list
#hash up