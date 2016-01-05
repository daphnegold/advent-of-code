with open('day1.txt', 'r') as puzzle:
    puzzletext = puzzle.read()
    up = puzzletext.count('(')
    down = puzzletext.count(')')

print(up-down)
