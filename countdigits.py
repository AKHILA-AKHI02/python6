def countdigits(s):
    d='0123456789'
    nd=0
    for i in s:
        if i in d:
            nd+=1
    return nd
inp=input("Enter a string:")
print("No of digits in ",inp,"is",countdigits(inp))
