def sum_natural_numbers(num):

    if num <= 1:
        return num
    else:
        return num + sum_natural_numbers(num - 1)

print(sum_natural_numbers(16))