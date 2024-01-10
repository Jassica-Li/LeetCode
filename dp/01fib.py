def fib(n):
    if n <= 2 : return 1
    return fib(n-1) + fib(n-2)

def fib_memoization(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2 : return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def fib_with_tabulation(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]