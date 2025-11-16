def is_palindrome(text):
    """
    Checks if a given string is a palindrome (reads the same forward and backward).

    The function ignores case and non-alphanumeric characters (like spaces).
    For example, "A man, a plan, a canal: Panama" is a palindrome.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # 1. Clean the string: remove non-alphanumeric characters and convert to lowercase.
    # We use a filter to keep only letters and numbers, then join them, and convert to lower case.
    cleaned_text = ''.join(filter(str.isalnum, text)).lower()

    # 2. Check for palindrome property: compare the cleaned string with its reverse.
    # Slicing [::-1] is the most Pythonic way to reverse a string.
    return cleaned_text == cleaned_text[::-1]

# --- Example Usage ---

# Test cases
test_string_1 = "racecar"
test_string_2 = "hello world"
test_string_3 = "Madam, in Eden, I'm Adam"

print(f"'{test_string_1}' is a palindrome: {is_palindrome(test_string_1)}")
print(f"'{test_string_2}' is a palindrome: {is_palindrome(test_string_2)}")
print(f"'{test_string_3}' is a palindrome: {is_palindrome(test_string_3)}")
