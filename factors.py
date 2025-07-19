def factors(n):
    count=0
    for i in range(1,n+1,1):
        if(inp%i==0):
            print(i,end=" ")
            count=count+1
inp=int(input("Enter a value:"))
print(factors(inp))               
