import datetime

class Shelf:
    def __init__(self):
        self.contents = []
    
    def additem(self, item):
        self.contents.append(item)

class Book:

    def __init__(self, name = "new book", author = "no author", pages = 0):
        self.type = "Book"
        self.name = name
        self.author = author
        self.pages = pages
        self.creation_date = datetime.date.today()

class Game:

    def __init__(self, name = "new game"):
        self.type = "Game"
        self.name = name
        self.creation_date = datetime.date.today()


if __name__ == "__main__":
    pass