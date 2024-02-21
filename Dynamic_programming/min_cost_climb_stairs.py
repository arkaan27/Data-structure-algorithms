"""
For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array.

Once you pay the cost for a step, you can either climb one or two steps. Find the minimum cost to reach the top of the
staircase. Your first step can either be the first or second step.

"""
import time


# The top-down recursive approach to solving the problem. This is very inefficient but first step
# to solving the problem
# Time: 2^N , Space: 2^N
def min_cost_climbing_stairs_td(cost):
    n = len(cost)
    return min(min_cost(n - 1, cost), min_cost(n - 2, cost))


def min_cost(i, cost):
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]
    return cost[i] + min(min_cost(i - 1, cost), min_cost(i - 2, cost))


# Memoizing our redundant recursive calls using dynamic programming
# Time: O(N), Space: O(N)
def min_cost_climbing_stairs_dp(cost):
    n = len(cost)
    dp = [None] * n
    return min(min_cost_dp(n - 1, cost, dp), min_cost_dp(n - 2, cost, dp))


def min_cost_dp(i, cost, dp):
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]
    if dp[i] is not None:
        return dp[i]
    dp[i] = cost[i] + min(min_cost_dp(i - 1, cost, dp), min_cost_dp(i - 2, cost, dp))
    return dp[i]


# Bottom up approach for solving
def min_cost_climbing_stairs_bu(cost):
    n = len(cost)
    return min(min_cost_bu(n - 1, cost), min_cost_bu(n - 2, cost))


def min_cost_bu(i, cost):
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]

    return cost[i] + min(min_cost_bu(i - 1, cost), min_cost_bu(i - 2, cost))


# Optimising the Space Complexity to O(1)
def min_cost_climbing_stairs_optimised(cost):
    n = len(cost)

    if n == 0:
        return 0
    if n == 1:
        return cost[0]
    dp_one = cost[0]
    dp_two = cost[1]
    for i in range(2, n):
        curr = cost[i] + min(dp_one, dp_two)
        dp_one = dp_two
        dp_two = curr

    return min(dp_one, dp_two)


if __name__ == "__main__":
    cost = [20, 15, 30, 5]
    start_time_td = time.time()
    print(min_cost_climbing_stairs_td(cost), f"Completed in {time.time() - start_time_td}")
    start_time_dp = time.time()
    print(min_cost_climbing_stairs_dp(cost), f"Completed in {time.time() - start_time_dp}")
    start_time_bu = time.time()
    print(min_cost_climbing_stairs_bu(cost), f"Completed in {time.time() - start_time_bu}")
    start_time_opti = time.time()
    print(min_cost_climbing_stairs_optimised(cost), f"Completed in {time.time() - start_time_opti}")
