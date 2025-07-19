def pattern(ch,n):
    temp=''
    for i in range(n,0,-1):
       temp=temp+i*ch+'\n'
    return temp
ch=input()
n=int(input('enter the value:'))
print(pattern(ch,n))
