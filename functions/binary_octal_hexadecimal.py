# decimal = 2
# for conversion will use inbuilt functions
# 
# 
# for i in range(0, 33):
#     print("the Octal value of",i,bin(i))

# print(bin(decimal))
# print(oct(decimal))
# print(hex(decimal))

# print(bin(0x2a))

# dec(bi)

def bin_to_decimal(num):
    decimal = 0
    temp = num
    count = 0
    while temp > 0:
        # print(num)
        digit = temp % 10 #temp=1011 -- chinu debugged 
        decimal = decimal + digit * pow(2,count)
        temp = temp // 10
        count = count +  1
    return decimal


def bin_to_decimal_int(num):
    return int(num, 2)

print(bin_to_decimal(1111))
print(bin_to_decimal_int('1011'))