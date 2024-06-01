n=int(input())

arr = []
dp=[[-1 for _ in range(n)]for _ in range(n)]
for i in range(n):    
	arr.append(list(map(int, input().split())))
dp[0][0]=arr[0][0]
for i in range(n):
	for j in range(n):
		if i==0 and j==0:
			continue
		if i==0:
			dp[i][j]=dp[i][j-1]+arr[i][j]
		elif j==0:
			dp[i][j]=dp[i-1][j]+arr[i][j]
		else:
			dp[i][j]=max(dp[i-1][j]+arr[i][j],dp[i][j-1]+arr[i][j])
print(dp[n-1][n-1])