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


# SECOND METHOD: TIME: O(n) | SPACE: O(n)
# Uses a list to keep track of items iterated on
# Finds the difference of the target sum & current item in array
# to find the possible second variable for the sum
# If the difference is not in the list, it will be add
# If it is in the list, then we have found our target sum
def two_number_sum_2(arr, target_sum):
    table = {}
    for n in arr:
        possible_val = target_sum - n
        if possible_val in table:
            return [possible_val, n]
        else:
            table[n] = True
    return []


# THIRD METHOD: VERY GOOD | TIME: O(n) | SPACE: O(1)
# Sorts First the arr, traverses both lower and higher sides of the array
# Takes the sum of both current higher & lower items of the array
    # if the sum is equal to the target sum, return both items
    # if the sum is less than the target, go to next lower value of array
    # if the sum is greater than the target, go to previous higher value of array
# Since array is sorted we know that the if the sum is lower than target,
# it would mean that the lower item is too small & we need to find the next greater value
# Vice versa
def two_number_sum_3(arr, target_sum):
    arr.sort()
    lower_index = 0
    higher_index = len(arr) - 1
    while lower_index < higher_index:
        l = arr[lower_index]
        r = arr[higher_index]
        sum = l + r
        if sum == target_sum:
            return [l, r]
        elif sum < target_sum:
            lower_index += 1
        elif sum > target_sum:
            higher_index -= 1
    return


print(two_number_sum_3([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
