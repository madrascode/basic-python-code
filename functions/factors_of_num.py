def factors_of_num(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(i)
factors_of_num(6)