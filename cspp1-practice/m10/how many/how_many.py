#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    var_c = 0
    for i in aDict:
        var_b = aDict[i]
        var_c += len(var_b)
    return var_c
animals = {'a':['anteater'],'b':['bat'],'c':['cat'],'d':['dog']}
print(how_many(animals))
"""def main():
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
    else:
        aDict[l[0][0]].append(l[1])
    print(how_many(aDict)


if __name__== "__main__":
    main()
"""
