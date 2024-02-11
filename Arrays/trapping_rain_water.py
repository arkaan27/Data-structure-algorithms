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


def getTrappedRainWaterBruteForce(A):
    # Time: O(N^2)
    # Space: O(1)
    totalWater = 0
    for x in range(0, len(A)):
        leftP = x
        rightP = x
        maxLeft = 0
        maxRight = 0
        while leftP >= 0:
            maxLeft = max(maxLeft, A[leftP])
            leftP -= 1
        while rightP <= len(A) - 1:
            maxRight = max(maxRight, A[rightP])
            rightP += 1
        currentWater = min(maxLeft, maxRight) - A[x]
        if currentWater >= 0:
            totalWater += currentWater

    return totalWater


def getTrappedRainWaterOptimisation(A):
    # Time: O(N)
    # Space: O(1)

    totalWater = 0
    p1 = 0
    p2 = len(A) - 1
    maxLeft = 0
    maxRight = 0

    # Logic for pointers
    while p1 < p2:
        if A[p1] <= A[p2]:
            if A[p1] >= maxLeft:
                maxLeft = A[p1]
            else:
                totalWater += maxLeft - A[p1]

            p1 += 1
        else:
            if A[p2] >= maxRight:
                maxRight = A[p2]
            else:
                totalWater += maxRight - A[p2]

            p2 -= 1
    return totalWater


if __name__ == '__main__':
    tc1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]  # 8
    tc2 = []  # 0
    tc3 = [3]  # 0
    tc4 = [3, 4, 3]  # 0
    tcs = [tc1, tc2, tc3, tc4]
    for tc in tcs:
        print("BruteForce Solutions")
        print(getTrappedRainWaterBruteForce(tc))
        print("Optimised Solution")
        print(getTrappedRainWaterOptimisation(tc))
