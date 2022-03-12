import tkinter
import time
from tkinter import Tk, Canvas
import random

import canvas as canvas

A_D_C_ = '#A2D3C2'
start = (3, 1)
end = (23, 17)

def drawMaze(maze, canvas: object):
    x1 = 0
    y1 = 0
    x2 = 30
    y2 = 30
    x = 0
    y = 0
    for row in maze:
        x1 = 0
        x2 = 30
        y = 0
        for i in row:
            if i == '+':
                canvas.create_rectangle(x1, y1, x2, y2, fill='#22333B', outline='#22333B')
            elif i == 's':
                canvas.create_rectangle(x1, y1, x2, y2, fill='#22333B', outline='#22333B')
                print("start: " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
            elif i == 'e':
                print("end: " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
            elif i == 'S':
                canvas.create_text(x1, y1, fill="#22333B", font="Times 20 italic bold",
                                   text="Start")
            elif i == 'E':
                canvas.create_text(x1 - 10, y1 - 20, fill="#22333B", font="Times 20 bold",
                                   text="Finish")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='white')
            x1 = x1 + 30
            x2 = x2 + 30
            y = y + 1

        x = x + 1
        y1 = y1 + 30
        y2 = y2 + 30


def get_maze():
    with open("mazetrix.txt") as f:
        lines = f.read().splitlines()
        return [line.strip() for line in lines]

#function to draw visited node/child in maze
def drawChild(canvas, x, y):
    x = x * 30
    y = y * 30
    canvas.create_rectangle(y, x, y + 30, x + 30, fill=('#A2D3C2'), outline='#A2D3C2')
    root.update()
    time.sleep(0.010)

#draw final path from start to end point
def drawPath(canvas, x, y):
    x = x * 30
    y = y * 30
    canvas.create_rectangle(y, x, y + 30, x + 30, fill='#CBA328', outline='#CBA328')
    root.update()
    time.sleep(0.010)

#bfs implementation
def bfs(maze, canvas):

    frontier = [start]
    explored = [start]
    drawChild(canvas, 3, 1)
    bfspath = {}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if matrix[currCell[0]][currCell[1]] == 'e':
            drawChild(canvas, currCell[0], currCell[1])
            bfspath[currCell] = (22, 17)
            break

        if matrix[currCell[0]][currCell[1]] != '+':
            # check up
            if currCell[0] > 0:
                if matrix[currCell[0] - 1][currCell[1]] == ' ' or matrix[currCell[0] - 1][currCell[1]] == 'e':
                    childcell = (currCell[0] - 1, currCell[1])
                    if childcell not in explored:
                        frontier.append(childcell)
                        explored.append(childcell)
                        bfspath[childcell] = currCell
                        drawChild(canvas, currCell[0] - 1, currCell[1])


            # check down
            if matrix[currCell[0] + 1][currCell[1]] == ' ' or matrix[currCell[0] + 1][currCell[1]] == 'e':
                childcell = (currCell[0] + 1, currCell[1])
                if childcell not in explored:
                    frontier.append(childcell)
                    explored.append(childcell)
                    bfspath[childcell] = currCell
                    drawChild(canvas, currCell[0] + 1, currCell[1])


            # check right
            if matrix[currCell[0]][currCell[1] + 1] == ' ' or matrix[currCell[0]][currCell[1] + 1] == 'e':
                childcell = (currCell[0], currCell[1] + 1)
                if childcell not in explored:
                    frontier.append(childcell)
                    explored.append(childcell)
                    bfspath[childcell] = currCell
                    drawChild(canvas, currCell[0], currCell[1] + 1)


            # check left
            if currCell[1] > 0:
                if matrix[currCell[0]][currCell[1] - 1] == ' ' or matrix[currCell[0]][currCell[1] - 1] == 'e':
                    childcell = (currCell[0], currCell[1] - 1)
                    if childcell not in explored:
                        frontier.append(childcell)
                        explored.append(childcell)
                        bfspath[childcell] = currCell
                        drawChild(canvas, currCell[0], currCell[1] - 1)
    TracePath(bfspath)

def TracePath(bfspath):
    cell = end
    fwdpath = {}
    while cell != start:
        fwdpath[bfspath[cell]] = cell
        cell = bfspath[cell]
    cell = end
    drawPath(canvas, cell[0], cell[1])
    print(fwdpath[bfspath[cell]])
    while cell != start:
        index = fwdpath[bfspath[cell]]
        print(index)
        drawPath(canvas, index[0], index[1])
        cell = bfspath[cell]


root = tkinter.Tk()
canvas = tkinter.Canvas()
canvas.configure(height=5000,width=5000,bg="#fff")
matrix = get_maze()
drawMaze(matrix, canvas)
canvas.pack()
root.update()

bfs(matrix, canvas)
canvas.pack()
root.update()

root.mainloop()
