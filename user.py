class Member:
    counter = 1
    def __init__(self, name: str):
        self.name = name
        self.id = str(Member.counter) 
        self.borrowed_books = []
        Member.counter += 1

    def __str__(self):
        return f"The member name is {self.name}, is library id number {self.id} "



    
        
