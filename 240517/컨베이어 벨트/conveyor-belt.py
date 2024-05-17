n, t = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = a + b


for _ in range(t):
    tmp = a[-1]
    for i in range(2*n-1, 0, -1):
        a[i] = a[i-1]
    a[0] = tmp

for i in range(n):
    print(a[i], end=' ')
print('')
for i in range(n):
    print(a[i+n], end=' ')