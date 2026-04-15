def solution(nums):
    my_dict = dict()
    for num in nums:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += 1
    
    return min(len(my_dict.keys()), len(nums) // 2)