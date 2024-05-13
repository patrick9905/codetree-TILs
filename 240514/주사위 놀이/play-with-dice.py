arr=[0]*7
lista=list(map(int,input().split()))

for i in lista:
    arr[i]+=1

for i in range(1,7):
    print(f"{i} - {arr[i]}")