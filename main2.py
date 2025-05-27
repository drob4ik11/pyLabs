class Book:
    def __init__(self, title, author, ratings):
        self.title = title
        self.author = author
        self.ratings = ratings

    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def ratings_greater_than(self, number):
        return [r for r in self.ratings if r > number]

    def __str__(self):
        return f"Назва: {self.title}, Автор: {self.author}, Середній рейтинг: {self.average_rating():.2f}"


class Ebook(Book):
    def __init__(self, title, author, ratings, file_size):
        super().__init__(title, author, ratings)
        self.file_size = file_size

    def __str__(self):
        return super().__str__() + f", Розмір файлу: {self.file_size} МБ"


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def library_average_rating(self):
        if not self.books:
            return 0
        total = sum(book.average_rating() for book in self.books)
        return total / len(self.books)

    def top_rated_book(self):
        if not self.books:
            return None
        return max(self.books, key=lambda book: book.average_rating())


if __name__ == "__main__":
    book1 = Book("Тіні забутих предків", "Михайло Коцюбинський", [4.5, 5, 3.5, 4])
    ebook1 = Ebook("1984", "George Orwell", [5, 4.5, 5, 4], 1.2)

    print(book1)
    print("Рейтинги > 4:", book1.ratings_greater_than(4))

    print(ebook1)

    library = Library("Міська бібліотека")
    library.add_book(book1)
    library.add_book(ebook1)

    print(f"\nСередній рейтинг у бібліотеці: {library.library_average_rating():.2f}")
    print("Найвища оцінена книга:", library.top_rated_book())
