n, m = input().split()

n = int(n)
m = int(m)
aQuantinty = []
a = input()
res = ''
carry = 0
for ai in a.split():
    resI = (carry+int(ai))//m
    carry = (carry+int(ai)) % m
    res+=str(resI)+' '

print(res)
#https://www.facebook.com/victor.velasquez.5492?fref=search&__tn__=%2Cd%2CP-R&eid=ARA3U9yWHXDSoCKzt9Ii6v80MWSOhwXkKZjY5VAxeWNq4Ls8H-UxqtaupCzCSk6RL6PO6VKWaT09TxU2