'''
            2 -> 4
1   -> 15 -> 2  -> 25  -> 3 -> 4
    1 -> 3
    1 <- 4

n =  [1.. n-1]   

0 roads io
1 roads i
2 roads o -> Impossible
'''



n, m = map(int,raw_input().split())
cacheIndexes = [0]*(n+1)
result = ''

def markCache(listToMark, mark ,a, b):
    if a < b:
        for x in range(a+1, b):
            if listToMark[x] == 0:
                listToMark[x] = mark
            else:
                listToMark[x] = 3
    else:
        for x in range(a+1, len(listToMark)):
            if listToMark[x] == 0:
                listToMark[x] = mark
            else:
                listToMark[x] = 3
        for x in range(0, b):
            if listToMark[x] == 0:
                listToMark[x] = mark
            else:
                listToMark[x] = 3

for x in range(1, m+1):
    a, b = map(int, raw_input().split())
    print(result,"res")
    print(cacheIndexes,"cache")
    if a > b:
        aux = a
        a = b
        b = aux
    if b - a -1 > n - b + a - 1:
        aux = a
        a = b
        b = aux
    if cacheIndexes[a] == 3 or cacheIndexes[b] == 3:
        result = 'Impossible'
        break
    if cacheIndexes[a] == 0 and cacheIndexes[b] == 0:
        markCache(cacheIndexes, 1, a, b)
        result+= 'i'
        continue
    if cacheIndexes[a] == 1 and cacheIndexes[b] == 1:
        result+='i'
        continue
    if cacheIndexes[a] == 1 or cacheIndexes[b] == 1:
        markCache(cacheIndexes, 2, a, b)
        result+='o'
        continue
    if cacheIndexes[a] == 2 and cacheIndexes[b] == 2:
        #markCache(cacheIndexes, 1, a, b)
        result+='o'
        continue   
    if cacheIndexes[a] == 2 or cacheIndexes[b] == 2:
        markCache(cacheIndexes, 1, a, b)
        result+='i'
        continue            
print(result)    


