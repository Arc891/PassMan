from PasswordManager import PasswordManager    
from Password import Password

def main():
    PM = PasswordManager()
    pw1 = Password.new()
    pw1.print()
    PM.add_password(pw1)
    PM.add_password(Password("Google", "user123", "password123", ["www.google.com"], "This is a note"))
    PM.add_password(Password("Facebook", "user123", "password123", ["www.facebook.com"], "This is a note"))
    PM.add_password(Password("Google", "user234", "password234", ["www.google.com"], "This is a note"))
    print(PM)
    PM.remove_password("Google")
    print(PM)
    return

if __name__ == "__main__":
    main()