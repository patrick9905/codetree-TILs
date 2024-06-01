def pibo(n):
    memo=[-1]*45
    if memo[n]!=-1:
        return memo[n]
    if n<=2:
        memo[n]=1
    else:
        memo[n]=pibo[n-1]+pibo[n-2]
    return memo[n]


n=int(input())
print(pibo(n))