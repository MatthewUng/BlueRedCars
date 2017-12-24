import matplotlib.pyplot as plt
import random 
from matplotlib.animation import FuncAnimation

length = 40
size = {10 : 2000, 
        20 : 500,
        40 : 100}
p = 0.30

fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1], frameon=True)
ax.set_xlim(0, length), ax.set_xticks([])
ax.set_ylim(0, length), ax.set_yticks([])


x,y,colors = [],[],[]
grid = [[None for _ in range(length)] for _ in range(length)]
turn = 'blue'
scat = None

def init():
    global scat

    for r in range(length):
        for c in range(length):
            if random.random() < p:
                color = 'red' if random.random() < 0.5 else 'blue'
                x.append(c+0.5)
                y.append(r+0.5)
                colors.append(color)

                grid[r][c] = [color, False]

    scat = ax.scatter(x,y,marker='s', s=size[length], color=colors)


def update(fr):
    for i in range(length):
        for j in range(length):
            if grid[i][j] != None:
                grid[i][j][1] = False

    def move_up(r, c):
        global x,y,colors
        new_r = r+1 if r+1 <length else 0
        
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
            move_right(r, new_c)
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
    x,y,colors = [],[],[]

    for r in range(length):
        for c in range(length):
            if grid[r][c] and grid[r][c][0] is 'blue':
                if turn is 'blue':
                    move_up(r,c)
                else:
                    x.append(c+0.5)
                    y.append(r+0.5)
                    colors.append('blue')

    for r in range(length):
        for c in range(length):
            if grid[r][c] and grid[r][c][0] is 'red':
                if turn is 'red':
                    move_right(r,c)
                else:
                    x.append(c+0.5)
                    y.append(r+0.5)
                    colors.append('red')

    scat.set_color(colors)
    scat.set_offsets(list(zip(x,y)))
    scat.set_sizes([size[length]]*len(x))

    turn = 'blue' if turn is 'red' else 'red'

animation = FuncAnimation(fig, update, interval=50, init_func=init)
plt.show()

