def fibonacci(num):
    # 0 1 1 2 3 5 8 13 fibonacci series
    # if num == 0 or num < 1:
    #     print(num)
    a = 0 
    b = 1
    print(a)
    print(b)
    while a + b <= num:
        c = a + b
        print(c)
        a = b
        b = c
        
fibonacci(100) 