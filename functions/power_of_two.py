def power_of_two(terms):
    result  = list(map(lambda i: 2** i, range(terms))) # power of two using anonomyous function 
    # here map takes the lambda function and put in the list format. 
    return result

print(power_of_two(10))