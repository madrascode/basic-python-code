# least common multiple is the smallest positive integer that is perfectly divisible by the given number
# lcm can only be equal to greater than or equal to bigger number ..so for that we need to find bigger number

from hcd_loops import loop_of_hcf

def lcm_num(num1, num2):
    if num1 < num2:
        bigger = num2
    else:
        bigger = num1
    while(True):
        if bigger%num1== 0 and bigger%num2 == 0: # will check whether both numbers are perfectly divisible with each other if they are then bigger number is our lcm
            lcm = bigger
            break
        bigger += 1 # if not will move our bigger pointer to next and will check again. 
    return lcm




print(lcm_num(12, 14))
print(loop_of_hcf(12, 14))

# from above print statement we can say that product of 12 X 14 = lcm X Hcf