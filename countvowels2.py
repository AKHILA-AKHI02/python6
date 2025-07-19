def countvowels(n):
    d="aeiouAEIOU"
    nd=0
    d.upper()
    for i in n:
        if i in d:
            nd+=1
    return nd
inps=input("Enter a string:")
print(countvowels(inps))
