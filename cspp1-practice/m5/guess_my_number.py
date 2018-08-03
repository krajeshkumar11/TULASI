#Guess My Number Exercise

def main():
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    a = input("Enter a number between 0 and 100:")
    l = 0
    h = 100
    ans = (l + h)//2
    print(ans)
    a1 = input("Enter either of h,l,c:")
    while a1 != "c":
        if a1 == "l":
            l = ans
            ans = (l+h)//2
            print(ans)
            a1 = input("Is your secret number"+str(ans)+"?"+"If not Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        else:
            h = ans
            ans = (l+h)//2
            print(ans)
            a1 = input("Is your secret number"+str(ans)+"?"+"If not Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    print("Your guessed number is:",ans)

main()
