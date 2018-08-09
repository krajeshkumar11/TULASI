"""
#Exercise : Assignment-1
#implement the function getAvailableLetters that takes in one parameter
- a list of letters, lettersGuessed.
This function returns a string that is comprised of lowercase English letters
 - all lowercase English letters that are not in lettersGuessed
"""
def getavailableletters(var_lettersguessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    var_a = list("abcdefghijklmnopqrstuvwxyz")
    var_b = sorted(var_lettersguessed)
    var_acopy = var_a[:]
    for i in var_acopy:
        if i in var_b:
            var_a.remove(i)
    return ''.join(var_a)
def main():
    """
    This function is to take input and call getavailableletters function.
    """
    var_n = input()
    for i in range(int(var_n)):
        data = input()
        var_l = data.split()
        var_l1 = []
        for j in var_l:
            var_l1.append(j[0])
        print(getavailableletters(var_l1))
if __name__ == "__main__":
    main()
