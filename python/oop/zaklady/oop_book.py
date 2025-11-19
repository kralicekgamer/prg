class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def about(self):
        return "Tato kniha se jmenuje " + self.name + " její autor je " + self.author + " a má " + str(self.pages) + " stran"
 
    def read(self, reader):
        return "Tuto knihu čte " + reader


first_book = Book("První kniha", "Michal Koláč", 67)
print(first_book.about())
print(first_book.read("Sigma"))