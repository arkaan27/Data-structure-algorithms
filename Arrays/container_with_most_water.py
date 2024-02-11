"""
You are given an array of positive integers where each
integer represents the height of vertical line
on a chart. Find two lines which together with the
x-axis forms a container that would hold the greatest
amount of water.
Return the area of water it would hold.


Assumptions:
1. Does the thickness of the lines affect the area?
    No, assume they take up no space
2. Do the left and right sides of the graph count as walls?
    No, the sides cannot be used to form container
3. Can we pick two values if one value is higher in the middle
    Yes, the value in the middle won't affect the container

"""


def most_water_brute_force(A):
    # Time: O(n^2)
    # Space: O(1)

    max_area = 0
    for x in range(0, len(A)):
        for y in range(x + 1, len(A)):
            height = min(A[x], A[y])
            width = y - x
            max_area = max(max_area, height * width)

    return max_area


def most_water_optimised(A):
    # Time: O(n)
    # Space: O(1)
    p1 = 0
    p2 = len(A) - 1
    max_area = 0
    # Calculate Area
    while p1 < p2:
        height = min(A[p1], A[p2])
        width = p2 - p1
        max_area = max(max_area, height * width)
        # Logic to move pointer
        if A[p1] <= A[p2]:
            p1 += 1
        else:
            p2 -= 1

    return max_area


if __name__ == '__main__':
    tc1 = [7, 1, 2, 3, 9]  # 28
    tc2 = []  # 0
    tc3 = [7]  # 0
    tc4 = [6, 9, 3, 4, 5, 8]  # 32
    tcs = [tc1, tc2, tc3, tc4]
    for tc in tcs:
        print("Brute Force Solutions")
        print(most_water_brute_force(tc))
        print("Optimised Solutions")
        print(most_water_optimised(tc))
