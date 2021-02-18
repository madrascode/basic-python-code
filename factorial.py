def fact_o_real(num):
    result = 1
    while num > 1:
        print(result)
        result *= num
         
        num = num -1
    return result

print(fact_o_real(5))

# factorial of 0 is 1
# factorial does not exist for negative number
