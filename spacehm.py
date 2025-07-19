def printreverse(s):
    temp=''
    for row in range(1,n+1,1):
        x=1
        for col in range(1,row+1):
          temp=temp+str(x)
          x=x+1
        temp=temp+'\n'
    return temp

n=int(input("enter the value:"))
print(printreverse(n))
