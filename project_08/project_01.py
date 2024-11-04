class Book:
    def __init__(self):
        self.title = input("책 이름 : ")
        self.author = input("저자 : ")
        self.price = int(input("가격 : "))

    def display(self):
        print("책 정보 : 제목 - ", self.title, "/ 저자 - ", self.author, "/ 가격 - ", self.price)

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.price == other.price
        return False

book1 = Book()
book2 = Book()

book1.display()
book2.display()
print(book1 == book2)
