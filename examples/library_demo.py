from library import Book, Library
from storage import save_library, load_library


# Demo of the Book and Library classes and JSON storage.
def main():
    book1 = Book("Dark matter", "Blake Crouch", "Sci-Fi", 150, bio="Multiple dimensions book with thrill and fights")
    book2 = Book("Kafka on the shore", "Murakami", "Dark", 300, bio="Talking cats etc")
    book3 = Book("Lord of the rings", "Tolkien", "Fantasy", 270, bio="Classic fantasy")

    librarybooks = [book1, book2, book3]

    library1 = Library(librarybooks)

    book1.set_rating(4.5)
    book1.write_review("Excellent book, would definitely recommend! ")
    book1.update_status("Read")

    save_library(library1, "storage.json")

    first_library = load_library("storage.json")

    print(first_library.books)


if __name__ == "__main__":
    main()
