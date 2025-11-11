class User:
    counter = 1
    def __init__(self, name: str):
        self.name = name
        self.id = str(User.counter) 
        self.borrowed_books = []
        User.counter += 1

    def __str__(self):
        return f"The member name is {self.name} {self.last_name}, is library id number {self.id} "



    
        