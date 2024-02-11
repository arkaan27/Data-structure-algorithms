"""
Given an array of integers representing an elevation
map where the width of each bar is 1, return how
much rainwater can be trapped

Assumptions:
1. Do the left and right sides of the graph count as walls?
    No, the sides are not walls
2. Will there be negative integers?
    No, Assume all integers are positive

Brute Force: Two pointer technique scanning left and right from each point

Optimised: Two pointer technique with logic to scan only once
"""


def get_trapped_rain_water_brute_force(A):
    # Time: O(N^2)
    # Space: O(1)
    total_water = 0
    for x in range(0, len(A)):
        left_p = x
        right_p = x
        max_left = 0
        max_right = 0
        while left_p >= 0:
            max_left = max(max_left, A[left_p])
            left_p -= 1
        while right_p <= len(A) - 1:
            max_right = max(max_right, A[right_p])
            right_p += 1
        current_water = min(max_left, max_right) - A[x]
        if current_water >= 0:
            total_water += current_water

    return total_water


def get_trapped_rain_water_optimisation(A):
    # Time: O(N)
    # Space: O(1)

    total_water = 0
    p1 = 0
    p2 = len(A) - 1
    max_left = 0
    max_right = 0

    # Logic for pointers
    while p1 < p2:
        if A[p1] <= A[p2]:
            if A[p1] >= max_left:
                max_left = A[p1]
            else:
                total_water += max_left - A[p1]

            p1 += 1
        else:
            if A[p2] >= max_right:
                max_right = A[p2]
            else:
                total_water += max_right - A[p2]

            p2 -= 1
    return total_water


if __name__ == '__main__':
    tc1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]  # 8
    tc2 = []  # 0
    tc3 = [3]  # 0
    tc4 = [3, 4, 3]  # 0
    tcs = [tc1, tc2, tc3, tc4]
    for tc in tcs:
        print("BruteForce Solutions")
        print(get_trapped_rain_water_brute_force(tc))
        print("Optimised Solution")
        print(get_trapped_rain_water_optimisation(tc))
