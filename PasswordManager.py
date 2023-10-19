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

    def add_password(self, password):
        if not isinstance(password, Password):
            raise TypeError("Password must be a Password object")
        
        self.passwords.append(password)
    
    def remove_password(self, name):
        options = []
        for password in self.passwords:
            if password.name == name:
                options.append(password)
        
        if len(options) == 0:
            print("Password not found")
        elif len(options) == 1:
            self.passwords.remove(options[0])
        else:
            print("Multiple passwords found")
            for i, password in enumerate(options):
                print(f"{i + 1}) {password}")
            choice = int(input("Which password would you like to delete? "))
            self.passwords.remove(options[choice - 1])
            
    def get_password(self, name):
        for password in self.passwords:
            if password.name == name:
                return password
        print("Password not found")