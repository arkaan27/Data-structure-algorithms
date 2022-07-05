"""
Valid Palindrome

A phrase is palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters
include letters and numbers

Given a string s, return true if it is a palindrome, or false otherwise.

"""
import re
from math import ceil


def isPalindromeBruteForce(s: str) -> bool:
    # left and right pointer approach
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    # left pointer starting at 0

    left = 0
    # Right pointer starting at the far right of string

    right = len(s) - 1

    while left < right:
        if not s[left] == s[right]:
            return False
        left += 1
        right -= 1

    return True


def isPalindromeBruteForceCentre(s: str) -> bool:
    # Lower casing the string and removing all spaces and extra characters
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    # Checking if len of string is even or odd
    if (len(s)) % 2 == 0:
        # Both pointers starting at the 2 centre position if even
        p1 = ceil((len(s) - 1) / 2)
        p2 = ((len(s)) // 2)
    else:
        # Both pointers starting at the centre of string if odd
        p1 = int(len(s) - 1) // 2
        p2 = int(len(s) - 1) // 2

    while p1 > 0 or p2 < len(s) - 1:
        if not s[p1] == s[p2]:
            return False
        p1 -= 1
        p2 += 1

    return True


def isValidPalindromeReversed(s: str) -> bool:
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    if s == s[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isPalindromeBruteForce(""))
    print(isPalindromeBruteForceCentre(""))
    print(isValidPalindromeReversed(""))
