
def ispalindrome(word):
    if len(word) < 2: 
        print(word, " is a palindrome")
        
    if word[0] != word[-1]: 
        print(word, " is not a palindrome")
        return
    return ispalindrome(word[1:-1])

def main():
    word = str(input("Enter a word: "))
    ispalindrome(word)

main()
