def printalpha(n):
    temp=''
    for row in range(1,n+1,1):
        x=66
        for col in range(1,row+1):
            temp=temp+str(x)
            x=x+1
        temp=temp+'\n'
    return temp
c=int(input("enter the value:"))
print(printalpha(c))
