def quick_select(numbers, k):
    if len(numbers) <= 1:
        return numbers
    pivot_index = partition(numbers)
    if k < pivot_index:
        return quick_select(numbers[:pivot_index], k)
    elif k > pivot_index:
        return quick_select(numbers[pivot_index + 1:], k - pivot_index)
    else:
        return numbers[pivot_index]


def partition(numbers):
    rp = len(numbers) - 1
    i = 0
    j = 0

    while j < rp:
        if numbers[j] < numbers[rp]:
            swap(numbers, i, j)
            i += 1
        j += 1

    swap(numbers, i, rp)
    return i


def swap(numbers, i, j):
    prev = numbers[j]
    numbers[j] = numbers[i]
    numbers[i] = prev
    return numbers


if __name__ == '__main__':
    numbers = [5, 3, 1, 6, 4, 2]
    answer = quick_select(numbers, 2)
    print(answer)