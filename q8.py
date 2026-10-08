#pattern
n=5
sp=5
for i in range(1 ,n+1):
    for s in range(0 ,sp):
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


#    
n=5
num=0
for i in range(n):
    for j in range(i+1):
       print(chr(65+num),end=" ")
       num+=1
    print()
    
#ABCD pattern pyramid
n=5
sp=5
for i in range(1,n+1):
    for s in range(0,sp):
        print(end=" ")
    for j in range(1,i+1):
        print(chr(65+j-1),end=" ")
    print()
    sp-=1
    
# ABCD pattern pyramid    
n = 5
for i in range(n):
    print("  "*(n-i-1),end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end=" ")
    print()
    
#ABCD pattern pyramid MISSING MIDDLE and show last row
n=5
for i in range(n):
    print("  "*(n-i-1),end=" ")
    for j in range(2*i+1):
        if(j==0 or j==2*i or i==n-1):
            print(chr(65+j),end=" ")
        else:
            print(" ",end=" ")
    print()
    
#* + pattern
n=5
for i in range(n):
    print("  "*(n-i-1),end=" ")
    for j in range(2*i+1):
        if(j==0 or j==2*i or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# * plus pattern
n=5
for i in range(n):
    print("  "*(n-i-1),end=" ")
    for j in range(2*i+1):
        if(j==0 or j==2*i or i==n-1 or j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * plus pattern    
n=5
for i in range(n):
    for j in range(n):
        if(i==n//2 or j==n//2):
            print("*",end=" ")
        else:      
            print(" ",end=" ")
    print()
    
    