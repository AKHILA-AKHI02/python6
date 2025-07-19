def printorder():
    temp=''
    for i in range(65,91,1):
        if i>77:
            temp=temp+chr(i+32)+','
        else:
            temp=temp+chr(i)+','
    return temp[0:-1]
print(printorder())
