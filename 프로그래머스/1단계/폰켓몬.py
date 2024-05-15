def solution(nums):
    maximum = len(nums) // 2
    new_list = []
    for i in nums:
        if i not in new_list and len(new_list) < maximum:
            new_list.append(i)
    return len(new_list)