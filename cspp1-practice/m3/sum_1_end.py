"""
Sum of first n numbers
"""
NUM = int(input("Enter number:"))
SUM = 0

for N in range(NUM + 1):
    SUM += N
    
print(SUM)
