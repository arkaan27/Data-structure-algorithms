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
    #     current_length = 0
    #     for y in range(x, len(S)):
    #         currentChar = S[y]
    #         if not string_tracker[currentChar]:
    #             current_length += 1
    #             string_tracker[currentChar] = True
    #             longest = max(current_length,longest)
    #         else:
    #             break
    #
    # return longest
    if len(S) <= 1:
        return len(S)
    max_length = 0
    for x in range(0, len(S)):
        string_tracker = []
        current_length = 0
        for y in range(x, len(S)):
            if not S[y] in string_tracker:
                current_length += 1
                string_tracker.append(S[y])
                max_length = max(current_length, max_length)
            else:
                break
    return max_length

    # string_tracker ={}
    # max_length = 0
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
    #             max_length = max(max_length, len(string_tracker))
    #             string_tracker.clear()
    # return max_length


def optimise_solution(S):
    if len(S) <= 1:
        return len(S)
    max_length = 0
    seen_char = {}
    p1 = 0
    p2 = 0
    for p2 in range(0, len(S)):
        if S[p2] not in S[p1:p2]:
            seen_char[S[p2]] = p2
            print(seen_char)
            p2 += 1
        else:
            max_length = max(max_length, p2 - p1)
            p1 = seen_char[S[p2]] + 1
            seen_char[S[p2]] = p2
            p2 += 1

    max_length = max(max_length, p2 - p1)

    return max_length


if __name__ == '__main__':
    tc1 = "abccabb"  # 3
    tc2 = "cccccc"  # 1
    tc3 = ""  # 0
    tc4 = "abcbda"  # 4
    tcs = [tc1, tc2, tc3, tc4]
    #
    for tc in tcs:
        print(optimise_solution(tc))
