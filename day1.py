def find_floor(puzzletext):
    up = puzzletext.count('(')
    down = puzzletext.count(')')
    return up - down

with open('day1.txt', 'r') as puzzle:
    puzzletext = puzzle.read()

print(find_floor(puzzletext))

for i in range(len(puzzletext)):
     if find_floor(puzzletext[0:i+1]) == -1:
         print(i+1)
         break
