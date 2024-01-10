def all_construct_with_recursion(target, word_bank):
    if len(target) == 0: return [[]]
     
    all_combinations = []
    for word in word_bank:
        if target.startswith(word):
            result_list = all_construct_with_recursion(target.replace(word,""), word_bank)
            for result in result_list:
                result.append(word)
            all_combinations += result_list
    return all_combinations

def all_construct_with_memoization(target, word_bank, memo={}):
    if target in memo: return memo[target]
    if len(target) == 0: return [[]]
    all_combinations = []
    for word in word_bank:
        if target.startswith(word):
            result_list = all_construct_with_memoization(target.replace(word,""), word_bank, memo)
            for result in result_list:
                result.append(word)
            all_combinations += result_list
    memo[target] = all_combinations
    return all_combinations

def all_construct_with_tabulation(target, word_bank):
    result_array = [None] * (len(target) + 1)
    result_array[0] = [[]]

    for i in range(len(result_array)):
        if result_array[i] is not None:
            for word in word_bank:
                if len(word) + i <= len(target) and target[i:len(word) + i] == word:
                    if result_array[i + len(word)] is None:
                        result_array[i + len(word)] = []
                    for combination in result_array[i]:
                        result_array[len(word) + i].append([word] + combination)
    return result_array[len(target)]

print(all_construct_with_tabulation("purple", ["purp", "p", "ur", "le", "purpl"]))


