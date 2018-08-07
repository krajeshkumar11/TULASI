# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(var_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    i = 0
    var_b = str(var_n)
    if i == (len(var_b) - 1):
        return int(var_b[i])
    else:
        return int(var_b[i]) + sumofdigits(int(var_b[(i + 1):]))


def main():
    # a = input()
    a = 234
    print(sumofdigits(int(a)))  

if __name__== "__main__":
    main()

