def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    rp = len(numbers) - 1
    i = 0
    j = 0
    while j < rp:
        if numbers[j] < numbers[rp]:
            swap(numbers, i , j)
            i += 1
        j += 1
    swap(numbers, i, rp)
    left_part = quick_sort(numbers[:i])
    right_part = quick_sort(numbers[i + 1:])
    return left_part + [numbers[i]] + right_part


def swap(numbers, i, j):
    prev = numbers[j]
    numbers[j] = numbers[i]
    numbers[i] = prev
    return numbers


if __name__ == '__main__':
    # numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    numbers = [5, 3, 1, 6, 4, 2]
    sorted_number = quick_sort(numbers)
    print(sorted_number)