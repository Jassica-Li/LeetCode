def can_construct_with_recursion(target, word_bank):
    # base case 1
    if len(target) == 0 : return True

    for word in word_bank:
        # base case 2, but I only focus on the "True" conditon
        if target.startswith(word):
            if can_construct_with_recursion(target.replace(word, ""), word_bank):
                return True
    return False

def can_construct_with_memoization(target, word_bank, memo = {}):
    # memoization
    for target in memo: return memo[target]
    # base case 1
    if len(target) == 0 : return True

    for word in word_bank:
        # base case 2, but I only focus on the "True" conditon
        if target.startswith(word):
            remainder_target = target.replace(word, "")
            if can_construct_with_memoization(remainder_target, word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

def can_construct_with_tabulation(target, word_bank):
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(len(target) + 1):
        if table[i]:
            for word in word_bank:
                if i + len(word) <= len(target) and target[i:i+len(word)] == word:
                    table[i + len(word)] = True
    return table[len(target)]