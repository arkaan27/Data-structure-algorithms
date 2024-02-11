"""
Given two strings S and T, return if they equal
when both are typed out. Any '#' that appears in the string
counts as backspace

Assumptions:
1. What happens when two #'s appear beside each other?
    Delete the two values before the first #.

2. What happens when there is no character to remove?
    It deletes nothing then, just like backspace would.

3. Are two empty strings equal to each other?
    Yes, consider two empty strings as equal.

4. Does case sensitivity matter?
    Yes it does, "a" does not equal "A"

Brute Force: Form an array for every character. If encountered with '#'
                pop the previous character.
                Compare the length of each array if its true then compare
                each character of the final array of each string


Optimised: Start with pointer at the end of the string.
            Start comparing every character of each String
            if encountered with '#' then skip the character comparison
            if

"""


def buildString(S):
    output_S = []
    for s in S:
        if s != "#":
            output_S.append(s)
        else:
            try:
                output_S.pop()
            except IndexError:
                pass
    return output_S


def backSpaceCompare(S, T):
    # Time: O(a + b)^2
    # Space: O(a + b)
    final_S = buildString(S)
    final_T = buildString(T)
    if len(final_S) != len(final_T):
        return False
    else:
        for x in range(0, len(final_S)):
            if final_S[x] != final_T[x]:
                return False

    return True


def backSpaceCompareOptimised(S, T):
    p1 = len(S) - 1
    p2 = len(T) - 1
    while p1 >= 0 or p2 >= 0:
        if S[p1] == '#' or T[p2] == '#':
            if S[p1] == '#':
                backCount = 2
                while backCount > 0:
                    p1 -= 1
                    backCount -= 1
                    if S[p1] == '#':
                        backCount += 2
            else:
                if T[p2] == '#':
                    backCount = 2
                    while backCount > 0:
                        p2 -= 1
                        backCount -= 1
                        if T[p2] == '#':
                            backCount += 2
        else:
            if not S[p1] == T[p2]:
                return False
            else:
                p1 -= 1
                p2 -= 1
    return True


if __name__ == '__main__':
    tc1 = ["ab#z", "az#z"]  # True
    tc2 = ["abc#d", "acc#c"]  # False
    tc3 = ["x#y#z#", "a#"]  # True
    tc4 = ["a###b", "b"]  # True
    tc5 = ["Ab#z", "ab#z"]  # False
    tcs = [tc1, tc2, tc3, tc4, tc5]

    for tc in tcs:
        print("Brute Force solution")
        print(backSpaceCompare(tc[0], tc[1]))
        print("Optimised Solution")
        print(backSpaceCompareOptimised(tc[0], tc[1]))
