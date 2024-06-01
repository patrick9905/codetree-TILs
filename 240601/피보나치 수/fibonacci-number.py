dp=[0]*100
dp[1]=1
dp[2]=1
for u in range(3,n+1):
    dp[u]=dp[u-2]+dp[u-1]
n=int(input())
print(dp(n))