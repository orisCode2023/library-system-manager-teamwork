class Member:
    counter = 1
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name
        self.id = Member.counter 
        self.borrowed_books = []
        Member.counter += 1

    def __str__(self):
        return f"The member name is {self.name} {self.last_name}, is library id number {self.id} "



    
        