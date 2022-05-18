# Conditional Execution
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
hrs = float(input("Enter hours"))
rate=float(input("Enter rate"))
if hrs>40:
        grosspay=rate*hrs+(hrs-40)*rate*0.5;
else:
        grosspay=hrs*rate;
print("grosspay=",grosspay)        
#debug
#python ActivitySet01/problem04.py 
#Enter hours:45 
#Enter rate10.5
#grosspay= 498.75