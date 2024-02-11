
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] >= numbers[j + 1]:
                prev = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = prev
            else:
                continue

    return numbers


if __name__ == '__main__':
    array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    n = bubble_sort(array)
    print(n)
