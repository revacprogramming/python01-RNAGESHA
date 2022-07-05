# Files
fhand=input("enter the file name:")
file=open(fhand,'r')
count=0
add=0
for line in file:
        if line.startswith('X-DSPAM-Confidence'):
                count+=1
                index=line.find(" ")
                y=line[index:]
                y=float(y)
                add+=y
average=add/count
print(f"average of the confidence:{average}")
                