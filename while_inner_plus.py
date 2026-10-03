# 1.Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus.
# This is to be done with a while loop. Note: the input will contain only integers or lists. 

def innermost_plus1(input_list):
    current = input_list
    while True:
        has_sublist = False
        for item in current:
            if isinstance(item, list):
                current = item
                has_sublist = True
                break
                
        if not has_sublist:
            break
    return [num + 1 for num in current]

input_list = [10,9,8,7,[6,5,4,[3,2]]]
    
problem_1 = innermost_plus1(input_list)

print(problem_1)
