# Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus.
# This is to be done with recursion. Note: the input will contain only integers or lists. 

def innermost_plus1_recursive(input_list):
    for item in input_list:
        if isinstance(item, list):
            return innermost_plus1_recursive(item)


    return [num + 1 for num in input_list]

input_list = [9,[8,7,[6,5,4,[3,2,1,0]]]] #For example
Problem_2 = innermost_plus1_recursive(input_list)
print(Problem_2)
    