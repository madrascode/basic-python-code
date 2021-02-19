def fibo_num(num):
    
    if num == 0 or num == 1:
        return num
    else:
        return fibo_num(num - 1) + fibo_num(num - 2)


fibo = []
for i in range(12):
    fibo.append(fibo_num(i))

print(fibo)