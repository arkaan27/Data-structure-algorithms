def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if target == numbers[mid]:
            return mid
        elif target < numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    x = binary_search(array, 6)
    print(x)