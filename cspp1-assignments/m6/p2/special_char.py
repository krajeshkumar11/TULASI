'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str_output = ""
    array_check = ["!","@","#","$","%","^","&","*"]
    for i in range(len(str_input)):
        temp_i = i
        if str_input[i] in array_check:
            str_output += str_input[:i] + " " + str_input[i + 1:]
            
    print(str_output)

if __name__ == "__main__":
    main()
