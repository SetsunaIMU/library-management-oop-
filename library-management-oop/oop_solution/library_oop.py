class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = available_copies
        self.available_copies = available_copies
        
    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        return f"{self.title} by {self.author} - {self.available_copies} copies available"  # Fixed format

class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book_id):
        if len(self.borrowed_books) >= 3:
            print(f"Error: {self.name} has reached borrowing limit (3 books).")
            return False
        if book_id in self.borrowed_books:  # Prevent borrowing same book twice
            print(f"Error: {self.name} has already borrowed this book.")
            return False
        self.borrowed_books.append(book_id)
        return True

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def __str__(self):
        return f"{self.name} ({len(self.borrowed_books)} borrowed)"
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_records = []

    def add_book(self, book_id, title, author, available_copies):
        if self.find_book(book_id):
            print(f"Error: Book ID {book_id} already exists!")
            return
        book = Book(book_id, title, author, available_copies)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        if self.find_member(member_id):
            print(f"Error: Member ID {member_id} already exists!")
            return
        member = Member(member_id, name, email)
        self.members.append(member)
        print(f"Member '{name}' registered successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return
        if not book:
            print("Error: Book not found!")
            return
        if book.available_copies <= 0:
            print(f"Error: No copies available!")  # Fixed message
            return

        if member.borrow_book(book_id) and book.borrow():
            # Remove any existing record for this member-book combination
            self.borrowed_records = [
                r for r in self.borrowed_records
                if not (r['member_id'] == member_id and r['book_id'] == book_id)
            ]
            self.borrowed_records.append({
                'member_id': member_id,
                'book_id': book_id,
                'member_name': member.name,
                'book_title': book.title
            })
            print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return

        if member.return_book(book_id) and book.return_copy():
            self.borrowed_records = [
                r for r in self.borrowed_records
                if not (r['member_id'] == member_id and r['book_id'] == book_id)
            ]
            print(f"{member.name} returned '{book.title}'")
        else:
            print(f"Error: This member hasn't borrowed this book!")  # Fixed message

    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(book)

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books: 
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books: 
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")

    def display_status(self):
        print("\n=== Library Status ===")
        for m in self.members:
            print(f"{m.name} ({m.id}): {len(m.borrowed_books)} book(s)")  
        print("\n=== Borrowed Records ===")
        for record in self.borrowed_records:
            print(f"{record['member_name']} has '{record['book_title']}'")
