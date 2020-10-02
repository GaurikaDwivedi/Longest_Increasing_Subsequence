def lis(a,n):
    out=[1]*n
    
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if a[j]>a[i]:
                continue
            possibleAns=out[j]+1
            if possibleAns>out[i]:
                out[i]=possibleAns

    best=0
    for i in range(n):
        if best<out[i]:
            best=out[i]
    return best        
    

n=int(input())
a=list(map(int,input().split()))
ans=lis(a,n)
print(ans)
