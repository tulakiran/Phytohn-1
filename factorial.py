def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
number = 5
result_recursive = factorial_recursive(number)
print(f"The factorial of {number} (using recursive approach) is: {result_recursive}")
