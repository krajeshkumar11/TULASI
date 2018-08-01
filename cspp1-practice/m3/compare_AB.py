"""
Third Program.
"""
print("1 for entering string and 2 for entering numbers")
VAR_C = int(input("Enter 1 or 2:"))
if VAR_C == 1:
    VAR_A = input("Enter a string:")
    VAR_B = input("Enter a string:")
    print("The two variables are strings.")
elif VAR_C == 2:
    VAR_A = int(input("Enter a number:"))
    VAR_B = int(input("Enter a number:"))
    if VAR_A > VAR_B:
        print("VAR_A is larger than VAR_B.")
    elif VAR_A == VAR_B:
        print("VAR_A is equal to VAR_B.")
    else:
        print("VAR_B is larger than VAR_A.")
else:
    print("Choose from the given two options.")
        
    
    
