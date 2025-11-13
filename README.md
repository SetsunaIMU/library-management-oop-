## Project Overview

A Python-based Library Management System that simulates real-world library operations. This object-oriented application allows librarians to manage book inventory, member registrations, and track borrowing activities with built-in validation for common library constraints.


## Project Structure

---
## Features
The `Book` class supports the following operations:

- `id` (int): Unique identifier for the book
- `title` (str): Book title
- `author` (str): Book author
- `total_copies` (int): Total copies owned by library
- `available_copies` (int): Currently available copies
- `borrow()`: Decrements available copies if books are available
- `return_copy()`: Increments available copies if return is valid
- `__str__()`: Returns formatted string with book details

The `Member` class supports the following operations:

- `id` (int): Unique member identifier
- `name` (str): Member's full name
- `email` (str): Contact email
- `borrowed_books` (list): List of currently borrowed book IDs
- `borrow_book(book_id)`: Adds book to borrowed list if under limit
- `return_book(book_id)`: Removes book from borrowed list
- `__str__()`: Returns member name and current borrow count

The `Library` class supports the following operations:

- `books` (list): Collection of Book objects
- `members` (list): Collection of Member objects
- `borrowed_records` (list): Transaction history of current borrows
- `add_book()`: Adds new book to inventory with duplicate ID prevention
- `add_member()`: Registers new member with duplicate ID prevention
- `find_book()`, `find_member()`: Helper methods to locate entities
- `borrow_book()`: Processes book borrowing with full validation
- `return_book()`: Processes book returns with validation
- `display_available_books()`: Shows all currently available books
- `display_member_books()`: Shows specific member's borrowed books
- `display_status()`: Comprehensive library status report

---
### Basic Operations
- **Adding Resources**: Books and members with duplicate ID prevention
- **Borrowing Process**: Successful book loans with copy tracking
- **Return Process**: Valid book returns with inventory updates
- **Information Display**: Available books and member borrowing status
---
### Edge Cases
- **Unavailable Books**: Attempting to borrow books with no available copies
- **Borrowing Limits**: Enforcing 3-book maximum per member
- **Invalid Returns**: Preventing returns of non-borrowed books
- **Non-existent Entities**: Handling requests for missing books/members
- **Last Copy Scenarios**: Managing when only one copy remains
---
### Requirements
- Python 3.x

---

##  How to Use
To run the demonstration script, execute `test_oop.py` from your terminal:
```bash
python test_oop.py
