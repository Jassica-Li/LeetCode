def can_sum_with_recusion(target_sum, numbers):
    if target_sum == 0: return True
    if target_sum < 0: return False

    for num in numbers:
        if can_sum_with_recusion(target_sum - num, numbers):
            return True
    return False

def can_sum_with_memoization(target_sum, numbers, memo={}):
    for target_sum in memo: return memo[target_sum]
    if target_sum == 0: return True
    if target_sum < 0: return False

    for num in numbers:
        if can_sum_with_memoization(target_sum - num, numbers, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False

def can_sum_with_tabulation(target_sum, numbers):
    result = [False] * (target_sum + 1)
    result[0] = True

    for i in range(target_sum+1):
        for  num in numbers:
            if i + num <= target_sum and result[i]:
                result[i+num] = result[i]
    return result[target_sum]