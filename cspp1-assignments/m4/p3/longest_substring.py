'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    str = input("Enter string")
    a = ""
    max_freq = 0
    start = 0
    end = 0
    for i in range(len(str)):
        flag = 0
        j = i
        a = str[j]
        while j < (len(str)-1) and flag == 0:
            if str[j] <= str[j+1]:
                a += str[j+1]
            else:
                flag = 1
            j = j + 1
        if max_freq < (j-i):
            max_freq = j-i
            start = i
            end = j 
    print(str[start:end])

main()

                
        
                

            