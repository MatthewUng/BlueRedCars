import numpy as np
import matplotlib.pyplot as plt
import random 
from matplotlib.animation import FuncAnimation

length = 5 
p = 0.3

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1], frameon=True)
ax.set_xlim(0, length), ax.set_xticks([])
ax.set_ylim(0, length), ax.set_yticks([])

#cars = np.zeros(length, dtype=[('car', bool), ('color'

x,y,colors = [],[],[]
grid = [[None for _ in range(length)] for _ in range(length)]
turn = 'blue'
scat = None

def init():
    global scat
    """
    for r in range(length):
        for c in range(length):
            if random.random() < p:
                #color = 'red' if random.random() < 0.5 else 'blue'
                color = 'red'
                x.append(c+0.5)
                y.append(r+0.5)
                colors.append(color)

                grid[r][c] = [color, False]
    """
    x = [0, 1, 1]
    y = [0, 0, 1]
    colors = ['red']*3
    grid[0][0] = ['red', False]
    grid[0][1] = ['red', False]
    grid[1][1] = ['red', False]

    scat = ax.scatter(x,y,marker='s', s=2000, color=colors)
    print('done init!')
    print(x)
    print(y)
    print(colors)


def update(fr):
    print("attempting to update")
    """
    for i in range(length):
        print(grid[i])
        """

    for i in range(length):
        for j in range(length):
            if grid[i][j] != None:
                grid[i][j][1] = False

    def move_up(r, c):
        global x,y,colors
        new_r = r+1 if r+1 <length else 0
        print('attempting to move', r,c, grid[r][c])
        
        if grid[r][c][1]:
            return

        if grid[new_r][c] == None:
            grid[new_r][c] = grid[r][c]
            grid[new_r][c][1] = True
            grid[r][c] = None
            x.append(c+0.5)
            y.append(new_r+0.5)
            colors.append(grid[new_r][c][0])

        elif grid[new_r][c][0] is grid[r][c][0] and not grid[new_r][c][1]:
            print('color:', grid[new_r][c][0], grid[r][c][0])
            grid[r][c][1] = True
            move_up(new_r, c)
            if grid[new_r][c]:
                grid[r][c][1] = True
                x.append(c+0.5)
                y.append(r+0.5)
                colors.append(grid[r][c][0])

            else:
                grid[new_r][c] = grid[r][c]
                grid[new_r][c][1] = True
                grid[r][c] = None
                x.append(c+0.5)
                y.append(new_r+0.5)
                colors.append(grid[new_r][c][0])

        else:
            grid[r][c][1] = True
            x.append(c+0.5)
            y.append(r+0.5)
            colors.append(grid[r][c][0])

    def move_right(r, c):
        global x,y,colors
        print('attempting to move right', r,c, grid[r][c])
        new_c = c+1 if c+1 < length else 0
        
        if grid[r][c][1]:
            return

        if grid[r][new_c] == None:
            grid[r][new_c] = grid[r][c]
            grid[r][new_c][1] = True
            grid[r][c] = None
            x.append(new_c+0.5)
            y.append(r+0.5)
            colors.append(grid[r][new_c][0])

        elif grid[r][new_c][0] is grid[r][c][0] and not grid[r][new_c][1]:
            grid[r][c][1] = True
            move_up(r, new_c)
            if grid[r][new_c]:
                grid[r][c][1] = True
                x.append(c+0.5)
                y.append(r+0.5)
                colors.append(grid[r][c][0])

            else:
                grid[r][new_c] = grid[r][c]
                grid[r][new_c][1] = True
                grid[r][c] = None
                x.append(new_c+0.5)
                y.append(r+0.5)
                colors.append(grid[r][new_c][0])

        else:
            grid[r][c][1] = True
            x.append(c+0.5)
            y.append(r+0.5)
            colors.append(grid[r][c][0])

    global x, y, colors 
    global turn
    turn = 'blue' if turn is 'red' else 'red'
    x,y,colors = [],[],[]
    for r in range(length):
        for c in range(length):
            if grid[r][c] and grid[r][c][0] is 'blue':
                continue
                move_up(r,c)

    for r in range(length):
        for c in range(length):
            if grid[r][c] and grid[r][c][0] is 'red':
                move_right(r,c)

    scat.set_color(colors)
    scat.set_offsets(list(zip(x,y)))
    scat.set_sizes([2000]*len(x))

animation = FuncAnimation(fig, update, interval=2000, init_func=init)
plt.show()

