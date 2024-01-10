def best_sum_with_recursion(target_sum,numbers):
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None
    for num in numbers:
        result = best_sum_with_recursion(target_sum - num, numbers)
        if result != None:
            combination = result + [num]
        if shortest_combination is None or len(combination) < len(shortest_combination):
            shortest_combination = combination
    return shortest_combination

def best_sum_with_memoization(target_sum, numbers, memo = {}):
   if target_sum in memo: return memo[target_sum]
   if target_sum == 0 : return []
   if target_sum < 0 : return None

   shortest_combination = None
   for num in numbers:
      result = best_sum_with_memoization(target_sum - num, numbers, memo)
      if result != None:
         combination = [num] + result
         if shortest_combination is None or len(combination) < len(shortest_combination):
            shortest_combination = combination

   memo[target_sum] = shortest_combination
   return shortest_combination

def best_sum_with_tabulatin(target_sum, numbers):
    result_array= [None] * (target_sum + 1)
    result_array[0] = []

    for i in range(target_sum + 1):
        if result_array[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    new_combination = result_array[i] + [num]
                    if result_array[i + num] is None or len(new_combination) < len(result_array[i] + [num]):
                        result_array[i + num] = new_combination
    return result_array[target_sum]