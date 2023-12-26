# create a class of linked_list (sorted by the value)
# add operation (no duplicates by value)
# delete operation
# clear operation. (all list)
# find operation


# Have a long array [] of fixed size, say 1000
# Each element of this array is a LinkedList of (key, value) pairs (initialize to an empty list)
# For each key, compute a number (hash) from this object
# Map this number to an index from 0 to 999, for example take (number % 1000)
# Add this (key, value) pair to the linked list at index (number % 1000) of the array.

# Get(key): Compute hash of key, then take (number % 1000).
# Search the linked list at index (number % 1000) until you find the (key, value) pair that matches key
# Use find operation of LinkedList here.


# Queue - FIFO - enqueue (add to tail)/dequeue(remove from head)
# Stack - LIFO - push (add to head)/pop(remove from head)

# Python program to demonstrate working of HashTable


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_book(self, data):
        node = Node(data)
        if self.head is None:
            # First element
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def enqueue(self, data):
        self.add_book(data)

    def dequeue(self):
        if self.head is None:
            return None
        result = self.head
        self.head = result.next
        return result

    def __str__(self):
        mystr = ""
        current = self.head
        while current is not None:
            mystr += "(" + str(current.data) + ") --> "
            current = current.next
        mystr += "None"
        return mystr

    # predicate is a function that takes data and returns True or False
    def find_book(self, predicate):
        found_list = []
        current = self.head
        while current is not None:
            if predicate(current.data):
                found_list.append(current.data)
            current = current.next
        return found_list

    # Delete ALL the nodes whose data make the predicate function True
    def delete_book(self, predicate):
        deleted_list = []
        current = self.head
        previous = None
        while current is not None:
            if predicate(current.data):
                deleted_list.append(current.data)
                if previous is not None:
                    previous.next = current.next
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = previous

            previous = current
            current = current.next
        return deleted_list

    def for_each(self, func):
        current = self.head
        while current is not None:
            func(current.data)
            current = current.next


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return self.title + " by " + self.author + " of " + str(self.pages) + " pages"


book1 = Book("Hobbit", "JRT", 1000)
book2 = Book("Harry Potter and the Philosopher's Stone", "JKR", 500)
book3 = Book("Lord of the Rings Fellowship of the Ring", "JRT", 2500)
book4 = Book("Harry Potter and the Prisoner of Azkaban", "JKR", 250)

list = LinkedList()
list.add_book(book1)
list.add_book(book2)
list.add_book(book3)
list.add_book(book4)

print("Running for each:")


def capitalize_title(book):
    book.title = book.title.upper()


# list.for_each(capitalize_title)

print("Initial list: " + str(list))

found_books = list.find_book(lambda b: b.author == "JRT")
print("Found books: " + str([str(book) for book in found_books]))

deleted_books = list.delete_book(lambda b: b.pages < 1000)

print("Deleted books: " + str([str(book) for book in deleted_books]))
print("Final list: " + str(list))

# TODO: Class olarak yap: class Hashtable:...

# Her bir eleman LinkedList olacak (bos)
# hashTable = [LinkedList] * 1000
# Use class method to generate Hashtable
# def hashFunction(key):

#     capacity = add_book(1000)
#     return key % capacity
#
#
# def findData(key, value):
#     index = hashFunction(key)
#     hashTable[index] = [key, value]
#
# def removeData(key):
#     index = hashFunction(key)
#     hashTable[index] = 0
#
# print(hashTable)


class Hashtable:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key] = value

    def has(self, key):
        return key in self.map

    def get(self, key):
        return self.map[key]

    def delete(self, key):
        del self.map[key]


hash_table = Hashtable()
hash_table.put(book1.title, book1)
hash_table.put(book2.title, book2)
hash_table.put(book3.title, book3)
hash_table.put(book4.title, book4)

print("Do we have Hobbit?: " + str(hash_table.has("Hobbit")))
print("Do we have Jurassic Park?: " + str(hash_table.has("Jurassic Park")))

print("Hobbit: " + str(hash_table.get("Hobbit")))
print(
    "Harry Potter and the Prisoner of Azkaban: "
    + str(hash_table.get("Harry Potter and the Prisoner of Azkaban"))
)
