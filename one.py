#check whether a number is positive, negative or zero
number=int(input("Input : "))
print("Output :")
if number>0:              #check for positive number
    print("Positive")
else:
    if number<0:          #check for negative number
        print("Negative")
    else:
        print("Zero")     #check for zero
