def is_prime(num):
    """
    Checks if a given number is a prime number.

    Args:
        num: An integer.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False  # Prime numbers are greater than 1
    
    # Check for divisibility from 2 up to the square root of num
    # We only need to check up to the square root because if a number 'n' has a divisor
    # greater than its square root, it must also have a divisor smaller than its square root.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

# Get input from the user
try:
    number = int(input("Enter a number to check for primality: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")