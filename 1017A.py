n = int(input())
gradesTotal = [None]*n

def sumGrades(strGrades):
    sum = 0;
    listGrades = strGrades.split()
    for idx, grade in enumerate(listGrades):
        #print("grade", grade)
        sum = sum + int(grade)
    return sum

for k in range(n):
    gradesTotal[k] = sumGrades(input())


#print(gradesTotal)
c = 1;
res = 1;
while c < len(gradesTotal):
    if gradesTotal[c] > gradesTotal[0]:
        res +=1
    c += 1;

print(res)
