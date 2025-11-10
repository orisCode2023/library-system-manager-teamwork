class Library:
    def __init__(self):
        self.lst_of_book = []
        self.lst_of_users = []

    def add_book(self,book):
        self.lst_of_book.append(book)
    
    def add_user(self,user):
        self.lst_of_users.append(user)
    
    def borrow_book(self,user_id, book_isbn):
        found_book = False
        for book in self.lst_of_book:
            if book_isbn == book.ISBN:
                found_book = True
                if user_id:
                    found_user = False
                    for user in self.lst_of_users:
                        if user_id == user.id:
                            found_user = True
                            if book.is_available:
                                print(f'The book "{book.title}" is available.')
                                user.borrowed_books.append(book_isbn)
                                book.change_status()
                            else:
                                print(f'The book "{book.title}" is currently unavailable.')
                            break
                    if not found_user:
                        print(f'No user found with ID {user_id}.')
                else:
                    print('Invalid user ID provided.')
                break
        if not found_book:
            print(f'No book found with ISBN {book_isbn}.')

    def return_book(self, user_id, book_isbn):
        found_book = False
        for book in self.lst_of_book:
            if book_isbn == book.ISBN:
                found_book = True
                if user_id:
                    found_user = False
                    for user in self.lst_of_users:
                        if user_id == user.id:
                            found_user = True
                            if book.is_available == True:
                                print(f'The book "{book.title}" has already been returned.')
                            else:
                                if book_isbn in user.borrowed_books:
                                    print(f'The book "{book.title}" has been returned.')
                                    user.borrowed_books.remove(book_isbn)
                                    book.change_status()
                                else:
                                    print(f'User {user_id} did not borrow the book "{book.title}".')
                            break
                    if not found_user:
                        print(f'No user found with ID {user_id}.')
                else:
                    print('Invalid user ID provided.')
                break
        if not found_book:
            print(f'No book found with ISBN {book_isbn}.')


    def list_available_books(self):
        available_books = []
        for book in self.lst_of_book:
            if book.is_available:
                available_books.append(book.title)
        return available_books
    
    
    def search_book(self,title):
        lst = self.list_available_books()
        for book in lst:
            if title == book.title:
                print(f'The book {title} is available')
            else :
                print(f'The book {title} is unavailable')

        

            
