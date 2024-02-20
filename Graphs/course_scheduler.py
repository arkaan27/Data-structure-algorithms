"""

There are a total of n courses to take, labeled from 0 to n-1

Some courses have prerequisite courses. This is expressed as a pair i.e. [1,0] which indicates you must take course 0
before taking course 1.

Given the total number of courses and an array of prerequisite pairs, return if it is possible to finish all courses.

Verify the Constraints:

Can we have courses unconnected to other courses?
Yes account for separate course chains.

"""


def can_finish(num_of_courses, prerequisites):
    adj_list = [[] for _ in range(num_of_courses)]

    for pre in prerequisites:
        adj_list[pre[1]].append(pre[0])

    def is_cyclic(course, visited, rec_stack):
        visited[course] = True
        rec_stack[course] = True

        for neighbor in adj_list[course]:
            if not visited[neighbor]:
                if is_cyclic(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[course] = False
        return False

    visited = [False] * num_of_courses
    rec_stack = [False] * num_of_courses

    # Check each course for cycles
    for course in range(num_of_courses):
        if not visited[course]:
            if is_cyclic(course, visited, rec_stack):
                return False

    return True


def can_finish_with_adj(num_of_courses, prerequisites):
    in_degree = [0] * num_of_courses
    adj_list = [[] for _ in range(num_of_courses)]

    for src, dest in prerequisites:
        in_degree[src] += 1
        adj_list[dest].append(src)

    stack = [i for i, degree in enumerate(in_degree) if degree == 0]

    count = 0

    while stack:
        current = stack.pop()
        count += 1

        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                stack.append(neighbor)

    return count == num_of_courses


if __name__ == "__main__":
    n = 6
    prerequisites = [
        [1, 0], [2, 1],
        [2, 5], [0, 3],
        [4, 3], [3, 5],
        [4, 5]
    ]
    print(can_finish(n, prerequisites))
    print(can_finish_with_adj(n, prerequisites))