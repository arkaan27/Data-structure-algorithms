import math


def merge_sort(numbers: list):
    if len(numbers) <= 1:
        return numbers

    middle = math.floor(len(numbers) / 2)

    left = numbers[:middle]
    right = numbers[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = list()
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


if __name__ == '__main__':
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    sorted_numbers = merge_sort(numbers)
    print(sorted_numbers)