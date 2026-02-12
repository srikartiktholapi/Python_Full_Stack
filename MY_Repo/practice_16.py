rows = int(input("enter the number of rows : "))
for i in range(0,rows+1):
    print("* " *i)

for i in range(1,rows+1):
    print(' '*(rows-i)+'*'*i)

for i in range(0,rows+1):
    print(" " *(rows-i) +"*"*(2*i-1)+" "*(rows-i))