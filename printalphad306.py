def printalpha(n):
    temp=''
    x=65
    for row in range(1,n+1,1):
        for col in range(row):
            temp=temp+chr(x)
            x=x+1
        temp=temp+'\n'
    return temp
c=int(input("enter the value:"))
print(printalpha(c))
