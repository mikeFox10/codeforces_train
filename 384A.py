n = int(input())

even = 'C.'*(n//2)
odd = '.C'*(n//2)

evenElem = even.count('C')
oddElem = odd.count('C')
total = 0

if n%2 != 0:
    even +='C'
    odd +='.'
    total += (evenElem + 1) * (n//2 + 1) + oddElem * ((n//2))

else:
    total += (evenElem + oddElem ) * n//2  

print(total)
for x in range(n):
    if x % 2 == 0:
        print(even)
    else:
        print(odd)