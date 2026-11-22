PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Classic Fiction', 'classic-fiction.jpg'),
(2, 'Science Fiction and Fantasy', 'science-fiction-fantasy.jpg'),
(3, 'Mystery', 'mystery.jpg'),
(4, 'Nonfiction', 'nonfiction.jpg');

-- Prices are sample store prices in US dollars, not live publisher quotes.
-- Image fields contain filenames only; image files are not needed for Part I.
INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, '1984', 'George Orwell', '9780451524935', 12.00, '1984.jpg', 1),
(2, 1, 'Pride and Prejudice', 'Jane Austen', '9780141439518', 9.00, 'pride-and-prejudice.jpg', 0),
(3, 1, 'To Kill a Mockingbird', 'Harper Lee', '9780061120084', 18.99, 'to-kill-a-mockingbird.jpg', 1),
(4, 2, 'Dune', 'Frank Herbert', '9780441172719', 12.99, 'dune.jpg', 1),
(5, 2, 'The Hobbit', 'J. R. R. Tolkien', '9780547928227', 16.99, 'the-hobbit.jpg', 0),
(6, 2, 'The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', '9780345391803', 8.99, 'hitchhikers-guide.jpg', 1),
(7, 3, 'And Then There Were None', 'Agatha Christie', '9780062073488', 12.99, 'and-then-there-were-none.jpg', 0),
(8, 3, 'Murder on the Orient Express', 'Agatha Christie', '9780062693662', 15.99, 'murder-on-the-orient-express.jpg', 1),
(9, 3, 'Sherlock Holmes: The Complete Novels and Stories Volume I', 'Arthur Conan Doyle', '9780553212419', 9.99, 'sherlock-holmes-volume-1.jpg', 0),
(10, 4, 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', '9780062316097', 29.99, 'sapiens.jpg', 0),
(11, 4, 'Educated', 'Tara Westover', '9780399590504', 28.00, 'educated.jpg', 1),
(12, 4, 'Atomic Habits', 'James Clear', '9780735211292', 27.00, 'atomic-habits.jpg', 1);

COMMIT;
