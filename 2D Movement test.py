yPos = 4;
yTop = 0;
yBot = 9;
xPos = 4;
xLef = 0;
xRig = 10;
ballXPos = 4;
ballYPos = 9;
grid = [];
for i in range(10):
    grid.append([])
    for j in range(22):
        grid[i].append('.')

grid[4][1] = "|"
grid[4][20] = "|"
grid[4][9] = "*"
def update():
    for i in range(10):
        print("".join(grid[i]))

def movPad(direction, pos):
    if direction.lower() == 'up':
        if pos > yTop:
            grid[pos][1] = '.'
            grid[pos-1][1] = '|'
            return pos-1
        else:
            return pos
        
    elif direction.lower() == 'down':
        if pos < yBot:
            grid[pos][1] = '.'
            grid[pos+1][1] = '|'
            return pos+1
        else:
            return pos

    else:
        return pos
def enemy(xPos):
    grid[xPos][20] = '.'
    grid[xPos+1][20] = '|';
    
def ballX(xPos):
    return xPos - 1;

def ballY(yPos):
    return yPos - 1;
def ballMove():
    
    grid[ballXPos+1][ballYPos+1]='.'
    grid[ballXPos][ballYPos]='*'
update()

while True:
    ud = input('ud: ')
    yPos = movPad(ud, yPos)
    enemy(ballXPos)
    ballXPos = ballX(ballXPos)
    ballYPos = ballY(ballYPos)
    ballMove();
    update()
