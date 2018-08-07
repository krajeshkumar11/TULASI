"""
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and
returns the factorial of given number.
# This function takes in one number and returns one number.
"""
def factorial(var_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if var_n == 1:
        return 1
    else:
        return var_n * factorial(var_n - 1)
def main():
    """
    This function is to call the factorial function.
    """
    var_a = input()
    print(factorial(int(var_a)))
if __name__ == "__main__":
    main()
