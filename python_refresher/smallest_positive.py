def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_positive = None

    # First assign the first number greater than 0 to the result
    for num in in_list:
    	if num > 0:
    		smallest_positive = num
    		break

    # Iterate through the list and check each for being smaller than
    # current smallest yet greater than 0, then return result.
    for num in in_list:
    	if num < 0:
    		continue
    	elif num < smallest_positive and num > 0:
    		smallest_positive = num
    	else:
    		continue

    return smallest_positive

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([88.22, -17.41, -26.53, 18.04, -44.81, 7.52, 0.0, 20.98, 11.76]))
# Correct output: 0.2