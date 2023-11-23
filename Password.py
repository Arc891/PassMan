class Password:
    def __init__(self, name, username, password, websites: list[str] = [], notes: str = None):
        self.name = name
        self.username = username
        self.password = password
        self.websites = websites
        self.notes = notes
    
    def __str__(self) -> str:
        return f"{self.name} - {self.username}"
    
    def __repr__(self) -> str:
        return f"Password(name={self.name}, username={self.username}, password={self.password}, websites={self.websites}, notes={self.notes})"
    
    def new() -> "Password":
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")
        websites = input("Websites (separated by commas): ").split(",")
        notes = input("Notes: ")
        return Password(name, username, password, websites, notes)        

    def change_password(self, password: str) -> None:
        if not password or password.isspace() or type(password) != str:
            raise ValueError("Password cannot be empty")

        self.password = password
    
    def change_username(self, username: str) -> None:
        if not username or username.isspace() or type(username) != str:
            raise ValueError("Username cannot be empty")

        self.username = username
    
    def add_website(self, website: str) -> None:
        if not website or website.isspace() or type(website) != str:
            raise ValueError("Website cannot be empty")
        
        self.websites.append(website)
    
    def remove_websites(self) -> None:
        self.websites = []

    def remove_website(self, website: str) -> None:
        if not website or website.isspace() or type(website) != str:
            raise ValueError("Website cannot be empty")

        for i, site in enumerate(self.websites):
            if site == website:
                self.websites.pop(i)
                return
        
        raise ValueError("Website not found")
    
    def remove_website_idx(self, website: int) -> None:
        self.websites.pop(website)
    
    def set_notes(self, notes: str) -> None:
        self.notes = str(notes)
    
    def remove_notes(self) -> None:
        self.notes = None
    
    def print(self) -> None:
        for entry in self.__dict__.items():
            print(f"{entry[0].capitalize()}: {entry[1]}")