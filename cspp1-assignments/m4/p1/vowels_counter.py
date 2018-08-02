#Assume var_input is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5
def main():
    var_input = input("Enter the string in lowercase only:")  # THIS IS STEP FOR ASKING USER INPUT.
    var_count = 0   # THIS VARIABLE IS USED TO KEEP THE COUNT OF VOWELS
    for var_character in var_input:
        if var_character == "a" or var_character == "e" or var_character == "i" or var_character == "o" or var_character == "u":   # THIS LINE IS TO CHECK WHETHER THERE ARE ANY VOWELS. 
            var_count += 1       # ITERATION STEP IF LOOP IS EXECUTED.
    print(var_count)    # PRINT STATEMENT

main()

	
