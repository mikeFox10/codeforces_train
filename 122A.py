n = input()




def isLucky(n):
    for x in n:
        if x != '7' and x != '4':
            return False
    return True

def ckeckIsAlmostLucky(n):
    if isLucky(n):
        return 'YES'
    for x in range(3,int(n)//2 + 1):
        if isLucky(str(x)) and int(n)%x == 0:
            return 'YES'
    return 'NO'

print(ckeckIsAlmostLucky(n))


# range ([init, end[)