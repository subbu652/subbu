def operationchoices(c, a, b):
    if c == 1:
        return a + b
    elif c == 2:
        return a - b
    elif c == 3:
        return a * b
    elif c == 4:
        # Checking if b is not 0 to avoid division by zero
        if b != 0:
            return a / b
        else:
            # Handling division by zero case
            print("Error: Division by zero!")
            return None  # You may choose to handle this case differently based on your requirements
    else:
        # Handling invalid choice
        print("Error: Invalid choice! Please choose a value between 1 and 4.")
        return None  # You may choose to handle this case differently based on your requirements

# Example usage
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

result = operationchoices(c, a, b)
if result is not None:
    print("Output:", result)
