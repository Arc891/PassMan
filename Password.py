class Password:
    def __init__(self, name, username, password, websites: list[str] = [], notes: str = None):
        self.name = name
        self.username = username
        self.password = password
        self.websites = websites
        self.notes = notes
    
    def __str__(self):
        return f"{self.name} - {self.username}"
    
    def __repr__(self):
        return f"Password(name={self.name}, username={self.username}, password={self.password}, websites={self.websites}, notes={self.notes})"
    
    def new():
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")
        websites = input("Websites (separated by commas): ").split(",")
        notes = input("Notes: ")
        return Password(name, username, password, websites, notes)        

    def change_password(self, password):
        self.password = password
    
    def change_username(self, username):
        self.username = username
    
    def add_website(self, website):
        self.websites.append(website)

    def remove_website(self, website):
        self.websites.remove(website)
    
    def add_notes(self, notes):
        self.notes = notes
    
    def remove_notes(self):
        self.notes = None
    
    def print(self):
        for entry in self.__dict__.items():
            print(f"{entry[0].capitalize()}: {entry[1]}")