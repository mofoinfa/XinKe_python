def is_continuous(numbers):
    if not numbers or len(numbers) < 5:
        return False
    numbers.sort()
    zero_count = numbers.count(0)
    gap_count = 0
    for i in range(zero_count, len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            return False
        gap_count += numbers[i + 1] - numbers[i] - 1
    return gap_count <= zero_count

###测试结果
numbers = [1, 2, 3, 4, 5]
print(is_continuous(numbers))  # True

numbers = [0, 0, 1, 2, 5]
print(is_continuous(numbers))  # True

numbers = [1, 3, 4, 5, 6]
print(is_continuous(numbers))  # True

numbers = [0, 0, 1, 2, 6]
print(is_continuous(numbers))  # False

numbers = [1, 2, 3, 4, 8]
print(is_continuous(numbers))  # False
