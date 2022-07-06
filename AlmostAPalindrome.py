"""

Given a string, determine if it is almost a palindrome.
A string is almost a palindrome if it becomes a palindrome
by removing 1 letter.
Consider only alphanumeric characters and ignore case sensitivity

"""


def validSubPalindrome(s: str, left: int, right: int):
    while left < right:
        if not s[left] == s[right]:
            return False
        left += 1
        right -= 1
    return True


def isAlmostPalindrome(s: str) -> bool:
    s = ''.join(ch for ch in s.lower() if ch.isalnum())
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left] == s[right]:
            return validSubPalindrome(s, left + 1, right) or validSubPalindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    tc1 = "raceacar" # True
    tc2 = "abccdba" # True
    tc3 = "abcdefdba" # False
    tc4 = "" # True
    tc5 = "a" # True
    tc6 = "ab" # True
    tcs = [tc1,tc2,tc3,tc4,tc5,tc6]
    for tc in tcs:
        print(isAlmostPalindrome(tc))
