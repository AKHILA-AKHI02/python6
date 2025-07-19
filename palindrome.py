def checkpalindrome(s):
    if s==s[::-1]:
        return "palindrome"
    else:
        return"not palindrome"
    return
inps=input("Enter a string:")
print(inps,"is",checkpalindrome(inps))
