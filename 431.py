def solve(a,boxes):
    totalWasteCalories = 0
    for box in boxes:
        totalWasteCalories += a[int(box)-1]
    return totalWasteCalories

if __name__ == "__main__":
    a = list(map(int,input().split()))
    boxes = input()
print(solve(a,boxes))
