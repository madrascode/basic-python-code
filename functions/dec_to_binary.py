def dec_to_bin(num):
    # 4 -> 4 % 2 - 0 - > 2% 2 - 0 ->1 % 2 -> 1
    # 1 0 0
    binary = ''
    result_arr = []
    while num > 0:
        digit = num % 2
        result_arr.append(digit)
        binary += str(digit)
        num //= 2
    
    result_arr.reverse()
    return result_arr

a = dec_to_bin(4)
print(a)
for i in a:
    print(i, end=" ")
