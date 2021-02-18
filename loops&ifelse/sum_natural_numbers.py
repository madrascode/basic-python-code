def sum_natural(num):
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    return sum

def sum_natural_formula(num):
    return num*(num+1)/2

print(sum_natural(5))
print(sum_natural_formula(5))