class Book:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn

class BorrowedBook:
    def __init__(self, book, borrower_name, borrow_date):
        self.book = book
        self.borrower_name = borrower_name
        self.borrow_date = borrow_date

class LibraryCatalog:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, title, author, publication_year, isbn):
        book = Book(title, author, publication_year, isbn)
        self.books.append(book)

    def borrow_book(self, book, borrower_name, borrow_date):
        borrowed_book = BorrowedBook(book, borrower_name, borrow_date)
        self.borrowed_books.append(borrowed_book)

    def search_by_title(self, title):
        results = []
        for book in self.books:
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def search_by_author(self, author):
        results = []
        for book in self.books:
            if author.lower() in book.author.lower():
                results.append(book)
        return results

    def display_books(self, book_list):
        if not book_list:
            print("No books found.")
            return
        print("{:<30} {:<20} {:<10} {:<15}".format("Title", "Author", "Year", "ISBN"))
        print("=" * 75)
        for book in book_list:
            print("{:<30} {:<20} {:<10} {:<15}".format(book.title, book.author, book.publication_year, book.isbn))

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("No books are currently borrowed.")
            return
        print("{:<30} {:<20} {:<10} {:<15} {:<20}".format("Title", "Author", "Year", "ISBN", "Borrower Name"))
        print("=" * 95)
        for borrowed_book in self.borrowed_books:
            book = borrowed_book.book
            print("{:<30} {:<20} {:<10} {:<15} {:<20}".format(book.title, book.author, book.publication_year, book.isbn, borrowed_book.borrower_name))

def main():
    library = LibraryCatalog()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search by Title")
        print("3. Search by Author")
        print("4. Borrow a Book")
        print("5. Display Borrowed Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            publication_year = input("Enter publication year: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, publication_year, isbn)
            print("Book added successfully.")
        elif choice == "2":
            title = input("Enter title to search for: ")
            results = library.search_by_title(title)
            library.display_books(results)
        elif choice == "3":
            author = input("Enter author to search for: ")
            results = library.search_by_author(author)
            library.display_books(results)
        elif choice == "4":
            title = input("Enter the title of the book to borrow: ")
            borrower_name = input("Enter your name: ")
            borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")
            book_to_borrow = None
            for book in library.books:
                if book.title.lower() == title.lower():
                    book_to_borrow = book
                    break
            if book_to_borrow:
                library.borrow_book(book_to_borrow, borrower_name, borrow_date)
                print("Book borrowed successfully.")
            else:
                print("Book not found in the catalog.")
        elif choice == "5":
            library.display_borrowed_books()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
