def evenodd(n):
    if(n%2==0):
        return(n,"is even")
    else:
        return(n,"is odd")
n=int(input("Enter the number:"))
print(evenodd(n))
