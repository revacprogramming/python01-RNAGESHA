# Loops & Iterators
i=1
while True:
    num1=input("enter the numbers")
    if num1=="DONE":
        break
    else:
        try:
            num1=int(num1)
            if i==1:
                largest=num1;
                smallest=num1;
                i=0;
            if largest<num1:
                largest=num1;
            if smallest>num1:
                smallest=num1;
        except:
            print("Invalid input");
            break
print("Maximum is",largest);
print("Minimum is",smallest);