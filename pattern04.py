def pattern(ch1,ch2,n):
    temp=''
    for i in range(1,n+1,1):
       temp=temp+ch1*(n-i)+ch2*(i)+'\n'
    return temp
ch1=input("Enter the character:")
ch2=input("Enter the character:")
n=int(input('Enter the number:'))
print(pattern(ch1,ch2,n))
