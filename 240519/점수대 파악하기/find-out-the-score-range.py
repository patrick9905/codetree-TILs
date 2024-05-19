list_num=list(map(int,input().split()))
list_score=[0]*11
for i in list_num:
    list_score[i//10]+=1
list_score[0]=0
for i in range(10,0,-1):
    print(f"{i}0 - {list_score[i]}")