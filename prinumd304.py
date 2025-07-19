def printpattern(n):
    temp=''
    x=1
    for row in range(1,n+1,1):
        for col in range(row):
          temp=temp+str(x)
          x=x+1
        temp=temp+'\n'
    return temp

n=int(input("enter the value:"))
print(printpattern(n))
