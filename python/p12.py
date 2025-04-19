def Checkpassword(password):
    # Check if the password has at least 4 characters
    if len(password) < 4:
        return 0

    # Check if the first character is a number
    if password[0].isdigit():
        return 0

    # Flags to track the presence of required elements
    has_digit = False
    has_uppercase = False

    # Iterate through the characters in the password
    for char in password:
        # Check for spaces or obliques
        if char.isspace() or char == '/':
            return 0

        # Check for at least 1 digit
        if char.isdigit():
            has_digit = True

        # Check for at least 1 uppercase letter
        if char.isupper():
            has_uppercase = True

    # Check if all conditions are met
    if has_digit and has_uppercase:
        return 1
    else:
        return 0

# Example usage
password = str(input(''))
output = Checkpassword(password)
print(f"Output: {output}")



