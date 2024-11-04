class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("title =", self.title)
        print("author =", self.author)
        print("price =", self.price)

book_1 = Book("A", "a", "3000")
book_2 = Book("B", "b", "4000")
book_1.display()

if book_1.price == book_2.price:
    print("True")
else:
    print("False")