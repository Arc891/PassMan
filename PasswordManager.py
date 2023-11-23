from Password import Password

class PasswordManager:
    def __init__(self):
        self.passwords = []

    def __str__(self):
        passwords = "".join([f"{password}\n" for password in sorted(self.passwords, key=lambda password: password.name)])
        return f"Passwords:\n{passwords}"

    def __repr__(self):
        passwords = "".join([f"{password.__repr__()}\n" for password in self.passwords])
        return f"PasswordManager(passwords={passwords})"

    def add_password(self, password) -> None:
        if not isinstance(password, Password):
            raise TypeError("Password must be a Password object")
        
        self.passwords.append(password)
    
    def remove_password(self, name) -> None:
        options = []
        for password in self.passwords:
            if password.name == name:
                options.append(password)
        
        if len(options) == 0:
            raise ValueError("Password not found")
        elif len(options) == 1:
            self.passwords.remove(options[0])
            return
        
        print("Multiple passwords found")
        for i, password in enumerate(options):
            print(f"{i + 1}) {password}")
        
        while True:
            choice = input(f"Which password(s) would you like to delete? [[0-9]+/(A)ll/(N)one] ")
            if choice == "A" or choice == "a":
                for password in options:
                    self.passwords.remove(password)
            elif choice.isdigit() and int(choice) <= len(options) and int(choice) > 0:
                self.passwords.remove(options[int(choice) - 1])
            elif not (choice == "N" or choice == "n"):
                print("Invalid input")
                continue
            return
    
    def remove_password(self, name, username) -> None:
        for password in self.passwords:
            if password.name == name and password.username == username:
                self.passwords.remove(password)
                return
        
        raise ValueError("Password not found")
            
    def get_password(self, name) -> list[Password] | None:
        pwds = []
        for password in self.passwords:
            if password.name == name:
                pwds.append(password)
        return pwds if pwds else None

    def get_password(self, name, username) -> Password | None:
        for password in self.passwords:
            if password.name == name and password.username == username:
                return password
        return None

    def update_password(self, old: Password, new: Password) -> None:
        if not isinstance(old, Password) or not isinstance(new, Password):
            raise TypeError("Password must be a Password object")
        
        for i, password in enumerate(self.passwords):
            if password.name == old.name and password.username == old.username:
                self.passwords[i] = new
                return
        
        raise ValueError("Password not found")