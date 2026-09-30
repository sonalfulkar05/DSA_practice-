#pattern
n=5
sp=5
for i in range(1,n+1):
    for s in range(0,sp):
        print(end=" ")
    for j in range(1,i+1):    
        print(j,end=" ")
    if(i!=1):
        print("1")
    print()
    sp-=1
    
#ABCDE pattern
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
    
#A BB CC PATTERN
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+i-1),end=" ")
    print()