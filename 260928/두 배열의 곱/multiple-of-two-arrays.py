arr1 = [list(map(int, input().split())) for _ in range(3)] 

arr2 = [list(map(int, input().split())) for _ in range(4)] 

for i in range(1,4):
    for j in range(3):
        
        print(arr2[i][j]*arr1[i-1][j],end=' ')
    print('')
