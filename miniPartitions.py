"""
Partitioning Into Minimum Number of Deci- Binary Numbers

A decimal number is called deci-binary if each of its digits
is either 0 or 1 without any leading zeros. For example, 101
and 1100 are deci-binary while 112 and 3001 are not.

Given a string n that represents a positive decimal integer,
return the minimum number of positive deci-binary numbers needed so
that they sum up to n.

"""


def isDeciBinaryNumber(x):
    y = str(x)
    if y[0] == 0:
        return False
    for c in y:
        print(c)
        if not (c == '1' or c == '0'):
            return False

    return True


def initialDeciNumber(n):
    deciNumber = '1'
    for x in range(0, len(n) - 1):
        deciNumber += '0'

    return int(deciNumber)


def minPartitions(n: str) -> int:
    if len(n) == 0:
        return 0
    numberMap = {}
    for c in n:
        if c == '0':
            numberMap[c] = 1
        else:
            numberMap[c] = int(c)
    minimumPartition = max(numberMap, key=numberMap.get)
    return int(minimumPartition)


def minPartitionsOptimised(n: str) -> int:
    if len(n) == 0:
        return 0
    else:
        return int(max(n))


if __name__ == '__main__':
    tc1 = '32'  # 3
    tc2 = ''  # 0
    tc3 = '82734'  # 8
    tc4 = '27346209830709182346'  # 9
    tcs = [tc1, tc2, tc3, tc4]
    for tc in tcs:
        print(minPartitionsOptimised(tc))
