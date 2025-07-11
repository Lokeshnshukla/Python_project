# Password Strength Checker 


import re # regular expression module - it helps to search special character 

# password strength check condition:
# min 8 char, digit, uppercase, lowercase, special char

def check_password_strength(password):
    if len(password)<8:     # length of password 
        return "Weak: password must be atleast 8 characters"
    
    if not any (char.isdigit() for char in password):
        return "Weak: password must contain a digit."
    
    if not any(char.isupper() for char in password):
        return "Weak: password must contain an upper char"
    
    if not re.search(r'[!@#$%^&*()<>.?]', password):
        return "Medium: password must contain a special character"
    
    return "Strong: Your password is secured!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password( or type 'exit' to quit): ")

        if password.lower()=='exit':
            print("Thank you for using this tool.")
            break

        result= check_password_strength(password)
        print(result)

# Run the password_checker_tool 
if __name__ == "__main__":
    password_checker()

