"""
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
"""

def main():
    var_cube = int(input())
    var_guess = 1
    while (var_guess**3) < var_cube:
        var_guess += 1
    if int(var_guess**3) == var_cube:
        print(var_cube, "is a perfect cube")
    else:
        print(var_cube, "is not a perfect cube")

if __name__ == "__main__":
    main()
