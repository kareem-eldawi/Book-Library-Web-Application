class Book:
    """A book and its reading status, optional rating, and review."""

    def __init__(self, title, author, genre, pages, status="want to read", image=None, bio=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.rating = None
        self.review = None
        self.image = image
        self.bio = bio
        self.status = "want to read"
        self.update_status(status)

    def __repr__(self):
        return f"{self.title} by {self.author}"


    def set_rating(self, num):
        if self.status != "want to read":
            if 0 < num <= 5 and num % 0.5 == 0:
                self.rating = num

            else:
                return "Invalid rating, please try again"
        else:
            return "Cannot rate an unread book"

    def update_status(self, state):
        if state.lower() in ["read", "currently reading", "want to read"]:
            self.status = state.lower()
        else:
            return "Invalid status update"

    def write_review(self, rev):
        self.review = rev

    def to_dict(self):
        dictionary = {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": self.pages,
            "rating": self.rating,
            "review": self.review,
            "image": self.image,
            "status": self.status,
            "bio": self.bio,
        }

        return dictionary


class Library:
    """An in-memory collection with basic search, filtering, and sorting."""

    def __init__(self, books=None):
        self.books = []
        if books is not None:
            for b in books:
                self.books.append(b)


    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            return "Book not in collection"


    def find_by_title(self, title):
        matching_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                matching_books.append(book)

        return matching_books

    def filter_by_genre(self, genre):
        matching_genre = []
        for book in self.books:
            if book.genre.lower() == genre.lower():
                matching_genre.append(book)

        return matching_genre

    def filter_by_status(self, stat):
        matching_status = []
        for book in self.books:
            if book.status == stat.lower():
                matching_status.append(book)

        return matching_status

    def filter_by_rating(self, min_rating):
        matching_rating = []
        for book in self.books:
            if book.rating is not None and book.rating >= min_rating:
                matching_rating.append(book)

        return sorted(matching_rating, key=lambda b: b.rating, reverse=True)

    def sort_by_title(self):
        return sorted(self.books, key=lambda b: b.title.lower())
