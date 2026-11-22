import math
import sqlite3
from pathlib import Path

DB_NAME = Path(__file__).resolve().with_name("bookstore.db")


def print_divider() -> None:
    print("\n" + "-" * 40)


def pause() -> None:
    input("\nPress Enter to continue...")


def print_menu() -> None:
    print_divider()
    print("Bookstore Menu")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. Quit")
    print("9. View readNow books (extra feature)")


def welcome_screen() -> None:
    print_divider()
    print("Welcome to the Bookstore CLI")
    print("Use the menu to browse and manage your books.")
    pause()


def view_categories(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        "SELECT categoryId, categoryName, categoryImage FROM category ORDER BY categoryId"
    )
    rows = cursor.fetchall()
    print_divider()
    print("Categories")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No categories found.")


def view_books(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""
        SELECT bookId, title, author, price, image, readNow
        FROM book ORDER BY title
    """)
    rows = cursor.fetchall()
    print_divider()
    print("Books")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def view_books_in_category(cursor: sqlite3.Cursor) -> None:
    category_id = input("Enter a category id: ").strip()
    cursor.execute("""
        SELECT book.bookId, book.title, book.author, category.categoryName
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE category.categoryId = ?
        ORDER BY book.title
    """, (category_id,))
    rows = cursor.fetchall()
    print_divider()
    print("Books in category")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def search_by_title(cursor: sqlite3.Cursor) -> None:
    keyword = input("Enter a title keyword: ").strip()
    cursor.execute("""
        SELECT bookId, title, author, price
        FROM book WHERE title LIKE ? ORDER BY title
    """, (f"%{keyword}%",))
    rows = cursor.fetchall()
    print_divider()
    print("Matching books")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def add_book(cursor: sqlite3.Cursor) -> None:
    try:
        category_id = int(input("Enter category id: ").strip())
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        price = float(input("Enter price: ").strip())
        image = input("Enter image filename: ").strip()
        read_now = int(input("Enter readNow (0 or 1): ").strip())
        if not all((title, author, isbn, image)):
            raise ValueError("Title, author, ISBN, and image filename are required.")
        if not math.isfinite(price) or price < 0:
            raise ValueError("Price must be a finite, nonnegative number.")
        cursor.execute("""
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (category_id, title, author, isbn, price, image, read_now))
        cursor.connection.commit()
        print_divider()
        print("Book added.")
    except (ValueError, OverflowError) as error:
        print_divider()
        print("Invalid input:", error)
    except sqlite3.IntegrityError as error:
        cursor.connection.rollback()
        print_divider()
        print("Database error:", error)


def update_price(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id: ").strip())
        new_price = float(input("Enter the new price: ").strip())
        if not math.isfinite(new_price) or new_price < 0:
            raise ValueError("Price must be a finite, nonnegative number.")
        cursor.execute(
            "UPDATE book SET price = ? WHERE bookId = ?",
            (new_price, book_id),
        )
        cursor.connection.commit()
        print_divider()
        if cursor.rowcount == 0:
            print("No book found.")
        else:
            print("Price updated.")
    except (ValueError, OverflowError) as error:
        print_divider()
        print("Invalid input:", error)
    except sqlite3.IntegrityError as error:
        cursor.connection.rollback()
        print_divider()
        print("Database error:", error)


def delete_book(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id to delete: ").strip())
        cursor.execute("DELETE FROM book WHERE bookId = ?", (book_id,))
        cursor.connection.commit()
        print_divider()
        if cursor.rowcount == 0:
            print("No book found.")
        else:
            print("Book deleted.")
    except (ValueError, OverflowError) as error:
        print_divider()
        print("Invalid input:", error)


def view_read_now(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""
        SELECT bookId, title, author, price
        FROM book WHERE readNow = ? ORDER BY title
    """, (1,))
    rows = cursor.fetchall()
    print_divider()
    print("Read now books")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No books found.")


def main() -> None:
    if not DB_NAME.is_file():
        print("bookstore.db is missing. Follow README.md to create it first.")
        return
    connection = sqlite3.connect(DB_NAME)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("SELECT bookId FROM book LIMIT 0")
        welcome_screen()
        while True:
            print_menu()
            choice = input("\nChoose an option: ").strip()
            if choice == "1":
                view_categories(cursor)
                pause()
            elif choice == "2":
                view_books(cursor)
                pause()
            elif choice == "3":
                view_books_in_category(cursor)
                pause()
            elif choice == "4":
                search_by_title(cursor)
                pause()
            elif choice == "5":
                add_book(cursor)
                pause()
            elif choice == "6":
                update_price(cursor)
                pause()
            elif choice == "7":
                delete_book(cursor)
                pause()
            elif choice == "8":
                print_divider()
                print("Goodbye!")
                break
            elif choice == "9":
                view_read_now(cursor)
                pause()
            else:
                print_divider()
                print("Invalid option. Try again.")
                pause()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
    except sqlite3.DatabaseError as error:
        print("Database error:", error)
        print("If the database is not initialized, follow README.md to rebuild it.")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
