class Book:
    counter = 100001 
    def __init__(self,title:str,author:str):
        self.title = title
        self.author = author
        self.ISBN = Book.counter
        self.is_available = True
        Book.counter += 13

    def change_status(self):
        
        self.is_available = not self.is_available
    def __str__(self):
        status = 'Available' if self.is_available else 'Checked out'
        return f'Title : {self.title}\nAuthor : {self.author} \nISBN : {self.ISBN} \nStatus : {status}'
               
               
                
        
    
