def running_sum(nums):
        result = []
        sum = 0
        for i in nums:
            sum += i
            result.append(sum)
        print(result)
            

running_sum([1,2,3,4])