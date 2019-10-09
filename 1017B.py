n = int(input())
a = input()
b = input()

zerosInB=0
T10 = 0
T01 = 0
T00 = 0
T11 = 0

for idx, c in enumerate(b):
    if c == '0':
        if a[idx] == '1':
            T10 +=1
        else:
            T00 += 1
    else:
        if a[idx] == '0':
            T01 +=1
        else:
            T10 += 1

print(T01, T10)


T01 = T01*T10
zerosInB = b.count('0')
onesINA = a.count('1')


print((T10) * (zerosInB), "222")
print((zerosInB- T10) * (onesINA-T10) + (T10) * (zerosInB-T10)+ (onesINA-T10)*(zerosInB-T10))
