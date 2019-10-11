
def solve(colors):

    for color in colors:
        for i in range(0, len(color)):
            if color[i] == 'C' or color[i] == 'M' or color[i] == 'Y':
                return "#Color"

    return "#Black&White"


if __name__ == "__main__":
    n,m = list(map(int,input().split()))

    colors = []
    for _n in range(0,n):
        colors.append(input())

print(solve(colors))
