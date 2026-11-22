# Bookstore Database and Python CLI

**Name:** Hassan

This bookstore contains classic fiction, science fiction and fantasy, mystery,
and nonfiction: 4 categories with 3 books each, for 12 real books total.

## Files

`createTables.sql`, `insertRows.sql`, `bookstore.db`, `bookstore_cli.py`, and this README.

## Create the database

The included `bookstore.db` is already populated. To rebuild it, open a terminal
in this folder and run these commands with the SQLite command-line tool:

```bash
sqlite3 bookstore.db < createTables.sql
sqlite3 bookstore.db < insertRows.sql
```

Rebuilding deletes existing data and restores the sample catalog.

## Run the program

Use Python 3. No external Python packages are needed.

```bash
python3 bookstore_cli.py
```

Options 1-7 browse categories/books, filter by category, search titles, add a book,
update a price, and delete a book. Option 8 quits. **Extra feature:** option 9
shows only books with `readNow = 1`. Press Enter at each pause.

The CLI uses `?` parameters for user input, enables foreign keys, and saves each
successful change immediately. It opens the database beside the Python file.
ISBNs are stored as text. Enter a nonnegative price in USD and `readNow` as 0 or 1.
The catalog uses sample store prices. Image fields store filenames only;
actual image files are not needed.
