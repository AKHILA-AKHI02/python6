def fun(n):
    temp=''
    for i in range(1,n+1,1):
       temp=temp+s[0:i]+'\n'
    return temp
s=input("enter the string:")
n=int(input('Enter no of row(1-9):'))
print(fun(n))
