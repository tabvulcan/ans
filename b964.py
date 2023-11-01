input()
a=input().split()
a=list(map(int,a))
a.sort()
ma=-1
for i in range(60,101):
    if i in a:
        ma=i
        break
mi=-1
for i in range(59,-1,-1):
    if i in a:
        mi=i
        break
print(' '.join(list(map(str,a))))
if mi==-1:
    print('best case')
    print(ma)
elif ma==-1:
    print(mi)
    print('worst case')
elif ma==-1 and mi==-1:
    print('best case')
    print('worst case')
else:
    print(mi)
    print(ma)
