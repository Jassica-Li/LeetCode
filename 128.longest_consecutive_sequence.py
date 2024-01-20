def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    nums_set = set(nums)
    longest_streak = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    return longest_streak

def longest_consecutive_sequence_with_tabulation(nums):
    res_map = {_: 1 for _ in nums}

    for num in nums:
        if num-1 in res_map:
            res_map[num] += res_map[num - 1]




    
