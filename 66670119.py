n = int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    sum = (a+b+c)
    if(sum==180):
        print("YES")
    else:
        print("NO")