class Book:
    counter = 100001 
    def __init__(self,title:str,author:str,is_available:bool):
        self.title = title
        self.author = author
        self.ISBN = Book.counter
        self.is_available = is_available
        Book.counter += 13
    def __str__(self):
        return f'Title : {self.title}\nAuthor : {self.author} /nISBN : {Book.counter}'
               
               
                
        
    


        