"""
Given an array of integers, return the indices
of the two numbers that add up to a given target

Assumptions:
1. Are all the numbers positive or can there be negatives?
    All numbers are positive integers
2. Are there duplicate numbers in the array?
    No, there are no duplicates
3. Will there always be a solution available?
    No, there may not always be a solution available
    Return "null" when no solution is available
4. Can there be multiple pairs that add up to the target value?
    No, only 1 pair of numbers will add up to the target.

Brute Force: Two pointer- Pointer 1 finding the number to find
                          Pointer 2 matches the numberToFind with the rest of the array

Optimised Solution: Uses hashmap to record numberToFind and it's position
                        Search the array O(N) with a for loop to find the position of the next map value


"""

def two_sum_brute_force(A, T):
    # Time: O(n^2)
    # Space: O(1)

    ans = "null"

    for x in range(0, len(A)):
        number_to_find = T - A[x]
        for y in range(x + 1, len(A)):
            if number_to_find == A[y]:
                return [x, y]

    return ans


def two_sum_optimised(A, T):
    # Time: O(N)
    # Space: O(1)

    num_map = {}
    for x in range(0, len(A)):
        current_map_val = num_map.get(A[x])
        if current_map_val is not None and current_map_val >= 0:
            return [current_map_val, x]
        else:
            number_to_find = T - A[x]
            num_map[number_to_find] = x

    return "null"


if __name__ == "__main__":
    tc1 = [[1, 3, 7, 9, 2], 11]
    tc2 = [[1, 3, 7, 9, 2], 25]
    tc3 = [[], 5]
    tc4 = [[5], 5]
    tc5 = [[1, 6], 7]
    tcs = [tc1, tc2, tc3, tc4, tc5]
    for tc in tcs:
        print("Brute force solutions:")
        print(two_sum_brute_force(tc[0], tc[1]))
        print("Optimised Solutions")
        print(two_sum_optimised(tc[0], tc[1]))
