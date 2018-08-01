"""
Sum of first n numbers
"""
NUM = int(input("Enter number:"))
TEMP_NUM = 1
SUM = 0
while TEMP_NUM <= NUM:
    SUM += TEMP_NUM
    TEMP_NUM += 1
print(SUM)
