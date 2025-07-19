def printpattern(ch,n):
    temp=''
    for i in range(n,0,-1):
      temp=temp+ch*i+'\n' 
    return temp
ch=input()
n=int(input("enter the value:"))
print(printpattern(ch,n))
