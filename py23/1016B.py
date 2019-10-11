from sys import stdin, stdout  
n,m,q = stdin.readline().split()
s = stdin.readline().rstrip()
sub = stdin.readline().rstrip()
def countSubtrings(s,sub):
    resp = [0]*len(s)
    sum = 1
    for x in range(len(s)-len(sub)+1):
        if len(sub) == 1 and s[x] == sub:
            resp[x] = 1
            continue
        if s[x] == sub[0] and s[x:x+len(sub)] == sub:
            sum += 1
            resp[x+len(sub)-1] = 1
    return resp
def suma(listToSum):
    sum = 0
    for x in listToSum:
        sum+=x
    return sum

precalc = countSubtrings(s, sub)
#print(precalc)
resTotal = ''
cache = {}
for x in range(int(q)):
    l,r = stdin.readline().split()
    if l+'-'+r in cache:
        resTotal+= cache[l+'-'+r]
        continue
    if int(r) - int(l) + 2 <= len(sub):
        resTotal += '0\n'
        cache[l+'-'+r] = '0\n'
    else:
        calculated = str(suma(precalc[int(l)-1 + len(sub) - 1: int(r)]))+'\n'
        resTotal += calculated
        cache[l+'-'+r] = calculated
stdout.write(resTotal)