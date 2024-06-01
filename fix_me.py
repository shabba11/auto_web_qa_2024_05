def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count


numbers = [10, 15, 20]
result = calculate_average(nums=numbers)
print("The average is:", result)
