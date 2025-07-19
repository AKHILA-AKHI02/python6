def printorder():
    temp=''
    for i in range(65,91,1):
        if i%2==0:
            temp=temp+chr(i+32)+','
        else:
            temp=temp+chr(i)+','
    return temp[0:-1]
print(printorder())
