'''
use memo to avoid redundant caculation
'''
def fibonacci(n, memo={}):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Check if the value is already in the memo
    if n in memo:
        return memo[n]

    # Calculate the nth Fibonacci number recursively with memoization
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Example usage:
print(fibonacci(10))
'''
or the cache outside the function
'''
cache = {0: 0, 1: 1} #initalized with base case

def fibo(n):
    if n in cache:
        return fibo(n)
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]

#See recursion without memo:
def fibonaccii(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage:
print(fibonaccii(10))  # Output will be 55