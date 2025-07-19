def printday(daynum):
    if daynum==0:
        return"sunday"
    elif daynum==1:
        return"monday"
    elif (daynum==2):
        return"tuesday"
    elif (daynum==3):
        return"wendesday"
    elif (daynum==4):
        return"thrusday"
    elif (daynum==5):
        return"friday"
    elif (daynum==6):
        return"saturday"
daynum=int(input("Enter day number:"))
print(printday(daynum))    
