def differenceXOR(a, b):
    res = ''
    for i, j in zip(a, b):
        res = res+str(i ^ j)
    return res


if __name__ == '__main__':
    a = map(int, list(input().strip()))
    b = map(int, list(input().strip()))
    print(differenceXOR(a, b))

wc@