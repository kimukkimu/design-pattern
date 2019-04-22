from Book import Book
from Aggregate import Aggregate
from Iterator import Iterator

class BookShelf(Aggregate):
    def  __init__(self):
        self._books = []
        self._last = 0

    def getBookat(self, index: int) -> Book:
        return self._books[index]

    def appendBook(self, book: Book) -> None:
        self._books.append(book)
        self._last += 1

    def getLength(self) -> int:
        return self._last

    def iterator(self):
        return BookShelfIterator(self)



class BookShelfIterator(Iterator):
    def __init__(self, bookShelf :BookShelf):
        self._bookShelf = bookShelf
        self._index = 0

    def hasNext(self) -> bool:
        if (self._index < self._bookShelf.getLength()):
            return True
        else:
            return False

    def next(self) -> Book:
        book = self._bookShelf.getBookat(self._index)
        self._index += 1
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