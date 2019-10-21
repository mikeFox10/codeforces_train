k, a, b = map(int, raw_input().split())

res = 0
cache = {}
increment = 1



def getMultiplo(limit, k):
    return  limit//k;

if a < 0 and b > 0:
    res+=getMultiplo(b,k)
    res+=getMultiplo(abs(a),k)
    res +=1
else:
    if a<0 and b<=0:
        aux = a
        a = b
        b = aux
    a = abs(a)
    b = abs(b)
    res = getMultiplo(b,k) - getMultiplo(a,k)
    if a % k == 0:
        res+=1
    

print(res)