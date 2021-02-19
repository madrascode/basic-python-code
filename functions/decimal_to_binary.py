# def reverse_num(num):
#     for i in range(len(num)-1, -1, -1):
#         return(num[i])

# count_num('001')
# # from count_and_reverse import reverse_num
# def reverse_string(num):
#     result="" 
#     print("num value: ", num)
#     digit = 0
#     while int(num) > 0: 
#         digit = int(num)%10 # --> 001 % 10 - 1
#         print("digit value: ",digit)
#         result = str(digit) + result * 10
#         print("result: ",result)
#         num = int(num)//10
#         print("num value: ",num)
#     return str(result)

# print(reversDigits(int('001')))


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



# print(dec_to_bin(4))
# print(reverse_string('001'))

# #cinu ka code
# #decimal->binary
# #4->100
# #4//2=2...(0)
# #2//2=1...(0)
# #1//2=0...(1)
# # def function_cinuk(num):
# #     result = []
# #     while num / 2 != 0: # 4 // 2 - True  # 2 // 2  -- 1
# #         digit = num // 2 # 4 // 2 - 2  ---> 2 // 2 -> 1
# #         mod = num % 2 #  4 % 2 -- 0 --> 
# #         result.append(mod) # [0, 0]
# #         num = digit # 
# #     dec_t_bin  = result[::-1]
# #     return dec_t_bin
# # print(function_cinuk(4))


        

# #a//2
# #a%2= re1
# #a//2...qout=0...re1,re2