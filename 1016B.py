n,m,q = input().split()
s = input()
sub = input()
di = {}
def countSubtrings(s,sub):
    #print(l,r,s,sub, 'INPUT')
    resp = [0]*len(s)
    sum = 0
    for x in range(len(s)-len(sub)+1):
        #print(x,s[x:x+len(sub)])
        if s[x] == sub[0] and s[x:x+len(sub)] == sub:
            di[str(x)+str(x+len(sub))] = True
            resp[x] = sum
    return resp

precalc = countSubtrings(s, sub)
print(di)
print(precalc)

result = [None]*int(q)
for x in range(int(q)):
    l,r = input().split()
    #print(int(r) - int(l) , "lllrr")
    if int(r) - int(l) +1< len(sub):
        result[x] = 0
    else:
        result[x] = precalc[int(r)-len(sub)] - precalc[int(l)-1]

for q in result:
    print(q)
#aaaaaaaaaaaaaaaaaaaa