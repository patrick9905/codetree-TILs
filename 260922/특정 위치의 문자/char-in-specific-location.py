arr=['L','E','B','R','O','S']
n=input()
if n not in arr:
    print('None')
elif n in arr:
    print(arr.index(n))