class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    #действия, которые данный клас может делать
    def show_Book(self):
        print(f'Book: {self.title}, author: {self.author}, genre: {self.genre}')


my_Book = Book('Night watch', 'Alexander Belov', 'fantastic')
freinds_Book = Book('The secret materials', 'Dana Scully', 'fantastic')
my_Book.show_Book()
freinds_Book.show_Book()