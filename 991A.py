if __name__ == '__main__':
    a, b, c, n = map(int, input().split())
    passed = True
    presult = (a-c) + (b-c) + c 
    if (a-c < 0 or b-c < 0 or c<0):
        passed = False

    if(passed == False or (n-presult) < 1 or presult >= n):
        print(-1)
    else:
        print(n-presult)


## hacer bien el pseudo 
## nombrar bien las variables