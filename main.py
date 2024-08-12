import re

def passwordChecker(password):
    # Minimum length requirement
    min_length = 8

    # Check length
    if len(password) < min_length:
        return "Password must be at least 8 characters long."

    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check for digit
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    # Check for special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`|\\-]', password):
        return "Password must contain at least one special character."

    return "Password is strong."

def main():
    while True:
        password = input("Please enter your password: ")    
        result = passwordChecker(password)  # Call the function and store the result
        print(result)  # Print the result

        if result == "Password is strong.":
            break  # Exit the loop if the password is strong

if __name__ == "__main__":
    main()