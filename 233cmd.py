import hashlib
x="-61823470"
x = str(x)
if x[0:1] == '-':
    for i in x[1:len(x - 1)]:
        x = i + x
        x="-"+x
    num=int(x)
    if (-2**31)<num<(2**31-1):
        return num
    else:
        return 0
else:
    for i in x:
        x = i + x
    num=int(x)
    if (-2**31)<num<(2**31-1):
        return num
    else:
        return 0
