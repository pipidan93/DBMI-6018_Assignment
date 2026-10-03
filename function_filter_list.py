# Write a Python program that defines a standard function to filter a list of numbers. The function should accept two arguments:
    # A list of numbers
    # A user-defined threshold value
# The function should return a new list containing only the numbers that are less than or equal to the specified threshold. Values greater than the threshold should be excluded.

def filter_numbers(num_list, threshold):
    result_list = []
    for number in num_list:
        if number <= threshold:
            result_list.append(number)
    return result_list

# For example
input_nums = [3,8,10,4,9,5,2,0,12,1,15]
threshold_num = 6
problem_3 = filter_numbers(input_nums, threshold_num)
print(problem_3)