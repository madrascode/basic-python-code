def fact_o_real_recursion(num):
    if num <= 1:
        return 1
    else:
        return num * fact_o_real_recursion(num - 1)


for i in range(0,6):
    print(fact_o_real_recursion(i))