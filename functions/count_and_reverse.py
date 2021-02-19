def reverse_num(num):
    length = 0
    count = ""
    while int(num) > 0:
        rem =  int(num) % 10
        count += str(rem)
        num = int(num)// 10
        length += 1
    return count, length
    
print(reverse_num(123))