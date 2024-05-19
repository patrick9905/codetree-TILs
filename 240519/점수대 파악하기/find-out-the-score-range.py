list_num=list(map(int,input().split()))
list_score=[0]*11
for i in list_num:
    if i==0:
        break
    list_score[i//10]+=1
    
for i in range(10,0,-1):
    print(f"{i}0 - {list_score[i]}")