# here we have two inputs 
# input 1 is list from which we are going to find our result
# input 2 is the number for  which we have to check the number in the list divisible by input 2
def filter_num(list1, num):
    result  = list(filter(lambda x: (x % num == 0), list1))
    return result

num_after_filter = filter_num([2,5,8,32,56, 16,128], 8)

print(num_after_filter)