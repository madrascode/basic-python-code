def prime_interval(lower, upper):
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    # print(str(i)+" times "+str(num//i)+" is"+ str(num))
                    # print("Not Prime")
                    break
            else: # we have written this else block outside of for loop to ensure the prime no is not repeated till num value..
                print(num)

prime_interval(3, 11)