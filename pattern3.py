def pattern(s):
    temp=''
    for i in range(len(s),0,-1):
       temp=temp+s[0:i]+'\n'
    return temp
s=input('enter the string:')
print(pattern(s))
