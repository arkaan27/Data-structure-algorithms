"""
Given a string, find the length of the longest
substring without repeating characters.

Assumtions:
1. Is the substring contiguous?
    Yes, look for a substring not a subsequence

2. Does case sensitivity matter?
    No, assume all characters in the string are lowercase

"""

def solution(S):
    # if len(S) <= 1:
    #     return len(S)
    # longest = 0
    # for x in range(0, len(S)):
    #     string_tracker = {}
    #     currentLength = 0
    #     for y in range(x, len(S)):
    #         currentChar = S[y]
    #         if not string_tracker[currentChar]:
    #             currentLength += 1
    #             string_tracker[currentChar] = True
    #             longest = max(currentLength,longest)
    #         else:
    #             break
    #
    # return longest
    if len(S) <= 1:
        return len(S)
    maxLength = 0
    for x in range(0, len(S)):
        string_tracker = []
        currentLength = 0
        for y in range(x, len(S)):
            if not S[y] in string_tracker:
                currentLength += 1
                string_tracker.append(S[y])
                maxLength = max(currentLength, maxLength)
            else:
                break
    return maxLength

    # string_tracker ={}
    # maxLength = 0
    # if len(S) <= 1:
    #     return len(S)
    # x = 0
    # while x <= len(S) - 1:
    #     string_tracker[S[x]] = x
    #     print(string_tracker)
    #     for y in range(x+1,len(S)):
    #         if not S[y] in string_tracker:
    #             string_tracker[S[y]] = y
    #         else:
    #             maxLength = max(maxLength, len(string_tracker))
    #             string_tracker.clear()
    # return maxLength


def optimise_solution(S):
    if len(S) <= 1:
        return len(S)
    maxLength = 0
    seenChar = {}
    p1 = 0
    p2 = 0
    for p2 in range(0, len(S)):
        if S[p2] not in S[p1:p2]:
            seenChar[S[p2]] = p2
            print(seenChar)
            p2 += 1
        else:
            maxLength = max(maxLength, p2 - p1)
            p1 = seenChar[S[p2]] + 1
            seenChar[S[p2]] = p2
            p2 += 1

    maxLength = max(maxLength, p2 - p1)

    return maxLength


if __name__ == '__main__':
    tc1 = "abccabb" # 3
    tc2 = "cccccc" # 1
    tc3 = "" # 0
    tc4 = "abcbda" # 4
    tcs = [tc1, tc2, tc3, tc4]
    #
    for tc in tcs:
        print(optimise_solution(tc))
