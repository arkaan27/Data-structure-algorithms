"""
A company has n employees with unique IDs from 0 to n-1. The head of the company has ID 'head_id'.

You will receive a mangers array where managers[i] is the ID of the manager for employee i. Each employee has one direct
manager. The company head has no manager (managers[head_id] = -1). It's guaranteed the subordination relationships will
have a tree structure.

8 employees: 0, 1, 2, 3, 4, 5, 6, 7
head_id = 4
managers = [2, 2, 4, 6 , -1, 4, 4, 5]


The head of the company wants to inform all employees of news. He will inform his direct subordinates who will inform
their direct subordinates and so on until everyone knows the news.

You will receive an informTime array where inform_time[i] is the time it takes for employee i to inform all their direct
subordinates. Return the total number of minutes it takes to inform all employees of the news.

inform_time = [0, 0 , 4, 0 , 7, 3, 6, 0]

"""


def num_of_minutes(n, head_id, managers, inform_time):
    adj_list = [[] for _ in range(n)]

    for employee in range(n):
        manager = managers[employee]
        if manager == -1:
            continue
        adj_list[manager].append(employee)

    def dfs(curr_id):
        if not adj_list[curr_id]:
            return 0

        max_time = 0
        for subordinate in adj_list[curr_id]:
            max_time = max(max_time, dfs(subordinate))

        return max_time + inform_time[curr_id]

    return dfs(head_id)


if __name__ == "__main__":
    test_cases = [
        [8, 4, [2, 2, 4, 6, -1, 4, 4, 5], [0, 0, 4, 7, 3, 6, 0]],
        [1, 0, [-1], [0]],
        [7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]]
    ]

    for tc in test_cases:
        print(num_of_minutes(tc[0], tc[1], tc[2], tc[3]))
