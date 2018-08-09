#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    values = aDict.values()
    Biggest = 0
    word = 0
    for k in aDict:
        i = len(aDict[k])
        if Biggest < i:
        	Biggest = i
    return k
    
#animals = {'a':['animal'],'b':['ba','as'],'c':['a','f','g']}
#print(biggest(animals))
def main():
    aDict={}
    s=input()
    l=s.split()
    if l[0][0] not in aDict:
        aDict[l[0][0]]=[l[1]]
    else:
        aDict[l[0][0]].append(l[1])
        
    print(biggest(aDict))


if __name__== "__main__":
    main()
