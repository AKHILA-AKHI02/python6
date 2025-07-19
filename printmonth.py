def printmonth(month):
    if month==0:
        return"January"
    elif month==1:
        return"Febuary"
    elif (month==2):
        return"March"
    elif (month==3):
        return"April"
    elif (month==4):
        return"May"
    elif (month==5):
        return"June"
    elif (month==6):
        return"July"
    elif (month==7):
        return"August"
    elif (month==8):
        return"September"
    elif (month==9):
        return"October"
    elif (month==10):
        return"November"
    elif (month==11):
        return"December"
month=int(input("Enter month number:"))
print(printmonth(month))    
