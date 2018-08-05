"""
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
"""
def main():
    var_epsilon = 0.01
    var_num = int(input())
    var_guess = var_num/2.0
    while abs(var_guess*var_guess - var_num) >= var_epsilon:
        var_guess = var_guess - (((var_guess**2) - var_num)/(2*var_guess))
    print(str(var_guess))
if __name__ == "__main__":
    main()
