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
    var_num = int(input())
    var_epsilon = 0.01
    var_lower = 0.0
    var_higher = var_num
    var_bival = (var_higher + var_lower)/2.0
    while abs(var_bival**2 - var_num) > var_epsilon:
        if var_bival**2 < var_num:
            var_lower = var_bival
        else:
            var_higher = var_bival
        var_bival = (var_higher + var_lower)/2.0
    print(var_bival)
if __name__ == "__main__":
    main()
