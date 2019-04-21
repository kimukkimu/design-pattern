from Book import Book
from Aggregate import Aggregate
from Iterator import Iterator

class BookShelf(Aggregate):
    def  __init__(self):
        self.__books = []
        self.__last = 0

    def getBookat(self, index: int) -> Book:
        return self.__books[index]

    def appendBook(self, book: Book) -> None:
        self.__books.append(book)
        self.__last += 1

    def getLength(self) -> int:
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)



class BookShelfIterator(Iterator):
    def __init__(self, bookShelf :BookShelf):
        self.__bookShelf = bookShelf
        self.__index = 0

    def hasNext(self) -> bool:
        if (self.__index < self.__bookShelf.getLength()):
            return True
        else:
            return False

    def next(self) -> Book:
        book = self.__bookShelf.getBookat(self.__index)
        self.__index += 1
        return book



if __name__ == '__main__':
    bookShelf = BookShelf()
    bookShelf.appendBook(Book('Around the World in 80 days'))
    bookShelf.appendBook(Book('Bible'))
    bookShelf.appendBook(Book('Cinderella'))
    bookShelf.appendBook(Book('Daddy-Long-Legs'))
    it = bookShelf.iterator()
    while it.hasNext():
        book = it.next()
        print(book.getName())