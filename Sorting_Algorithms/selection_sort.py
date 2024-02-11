
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        p1 = i
        temp = numbers[i]
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[p1]:
                p1 = j
        numbers[i] = numbers[p1]
        numbers[p1] = temp
    return numbers


if __name__ == '__main__':
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    sorted_numbers = selection_sort(numbers)
    print(sorted_numbers)
