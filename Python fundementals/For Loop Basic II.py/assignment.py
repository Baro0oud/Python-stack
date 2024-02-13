# Biggie Size
def biggie_size(lst):
    return ["big" if num > 0 else num for num in lst]

# Count Positives
def count_positives(lst):
    positive_count = sum(1 for num in lst if num > 0)
    lst[-1] = positive_count
    return lst

# Sum Total
def sum_total(lst):
    return sum(lst)

# Average
def average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

# Length
def length(lst):
    return len(lst)

# Minimum
def minimum(lst):
    if not lst:
        return False
    return min(lst)

# Maximum
def maximum(lst):
    if not lst:
        return False
    return max(lst)

# Ultimate Analysis
def ultimate_analysis(lst):
    if not lst:
        return {}
    return {
        'sumTotal': sum_total(lst),
        'average': average(lst),
        'minimum': minimum(lst),
        'maximum': maximum(lst),
        'length': length(lst)
    }

# Reverse List
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Test the functions
print(biggie_size([-1, 3, 5, -5]))
print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))
print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))
print(average([1, 2, 3, 4]))
print(length([37, 2, 1, -9]))
print(length([]))
print(minimum([37, 2, 1, -9]))
print(minimum([]))
print(maximum([37, 2, 1, -9]))
print(maximum([]))
print(ultimate_analysis([37, 2, 1, -9]))
print(reverse_list([37, 2, 1, -9]))
