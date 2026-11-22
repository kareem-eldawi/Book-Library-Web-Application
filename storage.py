import json
import os

from library import Book, Library


def save_library(library, filename):
    """Save the library to a JSON file."""
    books = []
    for book in library.books:
        books.append(book.to_dict())

    with open(filename, "w") as f:
        json.dump(books, f, indent=4)


def dict_to_book(data):
    """Rebuild a Book, restoring its status before its rating."""
    new_book = Book(
        data["title"],
        data["author"],
        data["genre"],
        data["pages"],
        image=data["image"],
        status=data["status"],
        bio=data["bio"],
    )

    if data["rating"] is not None:
        new_book.set_rating(data["rating"])

    if data["review"] is not None:
        new_book.write_review(data["review"])

    return new_book


def load_library(filename):
    """Load saved books, or start empty if the JSON is missing or malformed."""
    book_list = []
    try:
        with open(filename, "r") as f:
            books = json.load(f)

    except FileNotFoundError:
        return Library()
    except json.JSONDecodeError:
        os.rename(filename, "broken_" + filename)
        return Library()

    for item in books:
        book_list.append(dict_to_book(item))

    library = Library(book_list)
    return library
