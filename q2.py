def is_palindrome(s):
  """
  Checks if a given string is a palindrome.

  Args:
    s: The input string.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Convert the string to lowercase and remove non-alphanumeric characters
  # to handle cases with different capitalization, spaces, and punctuation.
  processed_s = "".join(char.lower() for char in s if char.isalnum())
  
  # Compare the processed string with its reverse
  return processed_s == processed_s[::-1]

# Get input from the user
user_string = input("Enter a string to check if it's a palindrome: ")

# Check if the string is a palindrome and print the result
if is_palindrome(user_string):
  print(f"'{user_string}' is a palindrome.")
else:
  print(f"'{user_string}' is not a palindrome.")