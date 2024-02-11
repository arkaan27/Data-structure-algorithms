def binary_search(numbers, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if target == numbers[mid]:
            return mid
        elif target < numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_range(numbers, target):
    if len(numbers) == 0:
        return [-1, -1]
    first_pos = binary_search(numbers,0, len(numbers) - 1,
                              target)
    if first_pos == -1:
        return [-1, -1]
    start_pos = first_pos
    end_pos = first_pos
    temp1 = 0
    temp2 = 0
    while start_pos != -1:
        temp1 = start_pos
        start_pos = binary_search(numbers,0, start_pos - 1, target)
    start_pos = temp1

    while end_pos != -1:
        temp2 = end_pos
        end_pos = binary_search(numbers, end_pos + 1, len(numbers) - 1, target)

    end_pos = temp2

    return [start_pos, end_pos]


if __name__ == "__main__":
    array = [1, 3, 3, 5, 5, 5, 8, 9]
    x = search_range(array, 5)
    print(x)
