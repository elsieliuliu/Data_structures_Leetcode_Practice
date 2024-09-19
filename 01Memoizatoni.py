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