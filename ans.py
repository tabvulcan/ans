import datetime
td=input().split()
te=input().split()
td=list(map(int,td))
te=list(map(int,te))
t1=datetime.datetime(td[0], td[1], td[2])
t2=datetime.datetime(te[0],te[1],te[2])
print(abs((t2-t1).days)
