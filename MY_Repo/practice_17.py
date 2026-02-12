a =1 
while (a<10) :
    a = a+1 
    if a == 5 :
        print("found 5 ")
        break 

if __name__=="__main__" :
    x =int(input())
    y =int(input())
    z =int(input())
    n =int(input())
    print(x,y,z, "and value of n :", n)

    result =[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k !=n:
                    result.append([i,j,k])
    
    print(result)

a =60 
a=a<<2
print(a)
a=60
a=a>>2
print(a)

