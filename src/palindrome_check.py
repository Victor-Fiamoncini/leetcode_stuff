"""
Determine if a given string is a palindrome.
"""


def palindrome_check(input: str) -> bool:
    # Two pointers approach

    if len(input) == 0:
        return False

    left = 0
    right = len(input) - 1

    for _ in range(len(input)):
        if input[left] != input[right]:
            return False

        left += 1
        right -= 1

    return True
