n = int(input())
aiString = input()
visualized = [None]*3000
a = aiString.split()

for ai in a:
    visualized[int(ai)-1] = True

for index, v in enumerate(visualized):
    if not v:
        print(index+1)
        break