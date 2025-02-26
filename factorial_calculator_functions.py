def get_non_negative_integer() -> int:
    """
    Obtains a non-negative integer input from the user.
    Continuously prompts the user until a valid non-negative integer is entered.
    Returns:
        int: The validated non-negative integer.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
            else:
                print("Invalid input. Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.
    
    Args:
        n (int): The non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the given number.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main() -> None:
    """
    Main program flow to get input, calculate factorial, and display the result.
    """
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()
