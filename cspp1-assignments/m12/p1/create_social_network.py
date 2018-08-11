'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    var_data = data.splitlines()
    var_adict = {}
    if "follows" in data:
        for var_iterable1 in range(len(var_data)):
            var_listofindividual = var_data[var_iterable1].split(" ")
            #print(var_listofindividual)
            var_listofindividuals = var_listofindividual[2].split(",")
        #print(var_listofindividuals)
            for var_iterable2 in range(len(var_listofindividuals)):
                if var_listofindividual[0] not in var_adict:
                    var_adict[var_listofindividual[0]] = [var_listofindividuals[0]]
                else:
                    #print(len(var_listofindividuals))
                    var_adict[var_listofindividual[0]].append(var_listofindividuals[var_iterable2])
    return var_adict

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    #print(string)
    print(create_social_network(string))

if __name__ == "__main__":
    main()
