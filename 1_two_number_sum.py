""" 
    TWO SUM NUMBER:
    Finding two numbers in an array 
    that when summed up equals to 
    a target passed
"""


# FIRST METHOD: TIME: O(n^2) | SPACE: O(1)
# Traverses the array and while doing this,
# sums the current item with all remaining items in the array
# and compare the sum with the target_sum, if both are equal, the two items are returned
def two_number_sum_1(numbers, target):
    for i in range(len(numbers) - 1):
        first_num = numbers[i]
        for j in range(i + 1, len(numbers)):
            second_num = numbers[j]
            if first_num + second_num == target:
                return [first_num, second_num]

    return []
