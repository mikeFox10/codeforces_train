from sys import stdin, stdout  

def calculateWinner(squares):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    xs = squares.count('X')
    zs = squares.count('0')
    empty = 9 - xs - zs
    if xs -1 > zs or zs > xs :
        return 'illegal'
    flagWinner = 0
    countWinnersX = 0
    countWinnersZ = 0
    for i in range(len(lines)):
        a, b, c = lines[i];
        if ((squares[a] == 'X' or squares[a] == '0') and squares[a] == squares[b] and squares[a] == squares[c]):
            if squares[a] == 'X':
                flagWinner = 1
                countWinnersX+=1
            else:
                flagWinner = 2
                countWinnersZ+=1
    if countWinnersX >= 1 and countWinnersZ >= 1:
        return 'illegal'
    if flagWinner == 1:
        if zs < xs:
            return 'the first player won'
        else:
            return 'illegal' 
    elif flagWinner == 2:
        if zs == xs:
            return 'the second player won'
        else:
            return 'illegal' 
            
    if empty == 0:
        return 'draw'
    elif zs >=xs:
        return 'first'
    elif xs > zs:
        return 'second'
    return 'illegal';


def main(): 
	firstLine = stdin.readline().rstrip() 
	secondLine = stdin.readline().rstrip()
	thirdLine = stdin.readline().rstrip()
	stdout.write(calculateWinner(firstLine+secondLine+thirdLine) + '\n')

if __name__ == "__main__": 
	main()