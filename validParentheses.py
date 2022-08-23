"""

Given a string containing only parentheses, determine if it is valid. The string is valid if all parentheses close.

Example: "{ ( [ ] ) }"

Incorrect Example: "{ ( [ ] ) ]"
Incorrect Example: "{ ( [ ) ] }"
Incorrect Example: "{ ( [ ]"

Verify Constraints:

Does an empty string count as valid?
1. Yes, return true if string is empty


"""


def isValidParentheses(s: str):
    # Space : O(N)
    # Time: O(N)
    if len(s) <= 1:
        return True
    parens = {"(": ")",
              "[": "]",
              "{": "}"
              }
    stack = []
    for x in s:
        if x in parens:
            stack.append(x)
        else:
            if not stack:
                return False
            leftBracket = stack.pop()
            correctBracket = parens[leftBracket]
            if correctBracket != x:
                return False
    return not stack


if __name__ == '__main__':

    tc1 = ""  # True
    tc2 = "{([])} "  # True
    tc3 = "{ ( [ ]"  # False
    tc4 = "{ [ ( ] ) }"  # False
    tc5 = "{ [ ] ( ) }"  # True
    tcs = [tc1, tc2, tc3, tc4, tc5]

    for tc in tcs:
        print(isValidParentheses(tc))
