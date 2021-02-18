def i_am_strong(num):
    # a positive integer is called an arm strong number if abc  = a**3 + b**3 + c**3 
    # 153 = 1 ** 3 + 5 ** 3 + 3 ** 3
    # order of number
    # access each digit and put ** to it
    # sum all the exponented number
    # check if they are equal to num
    order = len(str(num))
    sum =0
    temp  = num
    while temp > 0:
        digit = temp % 10 # We can get our last digit by % 10...153 % 10 == 3 
        sum += digit ** order # so we got 3 from digit operation and now will apply exponent of order of num
        temp //= 10 # this will reduce our number to 0 and will exit the loop after temp < 0:
    if sum == num:
        return True

print(i_am_strong(153))