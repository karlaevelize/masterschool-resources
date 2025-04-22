# Check if all numbers are above 100
def is_all_above_100_method_1(numbers):

    # Control variable
    all_above_100 = True

    # Check if numbers are above 100
    for number in numbers:
        if number <= 100:
            all_above_100 = False

    # what should the function return?
    return all_above_100


def is_all_above_100_broken(numbers):
    for number in numbers:
        if number > 100:
            return True
        else:
            return False

def is_all_above_100(numbers):
    for number in numbers:
        if number <= 100:
            return False
    
    return True

print(is_all_above_100([240, 534, 300]))
