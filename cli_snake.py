import os
import time
import random

import keyboard

clear = lambda: os.system('clear')


gameField_width = 40
gameField_height = 20
global x, y, direction, state, fx,fy

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

PLAY = 0
END = 1

x = 4
y = 1
direction = RIGHT
state = PLAY

fx = 20
fy = 10

points = [[3,2],[2,1],[1,1]]


def check_point(pointx,pointy):
    global points
    point = [pointx,pointy]
    if point in points:
        return True
    else:
        return False
        
def snake_move(direction):
    global points, x, y, state
    
    head = points[0].copy()
    if direction == RIGHT:
        head[0] = head[0]+1
    elif direction == LEFT:
        head[0] = head[0]-1
    elif direction == UP:
        head[1] = head[1]-1
    elif direction == DOWN:
        head[1] = head[1]+1
    points.insert(0,head)
    points.pop()
    x = head[0]
    y = head[1]
    if x > gameField_width-2:
        x = gameField_width-2
        state = END
    elif x < 1:
        x = 1
        state = END
    if y > gameField_height-2:
        y = gameField_height-2
        state = END
    elif y < 1:
        y = 1
        state = END

def snake_eat():
    global points,fx,fy
    points.insert(0,[fx,fy])

def move(direction=RIGHT):
    global x,y, state
    if direction == RIGHT:
        x+=1
    elif direction == LEFT:
        x-=1
    elif direction == DOWN:
        y+=1
    elif direction == UP:
        y-=1
    
    if x > gameField_width-2:
        x = gameField_width-2
        state = END
    elif x < 1:
        x = 1
        state = END
    if y > gameField_height-2:
        y = gameField_height-2
        state = END
    elif y < 1:
        y = 1
        state = END

def draw():
    global x,y, state,fx, fy,head
    for i in range(gameField_height):
        for j in range(gameField_width):
            if i == 0 or i == gameField_height-1:
                if j == gameField_width-1:
                    print('#')
                
                else:
                    print('#', end='')
            else:
                
                if j == gameField_width-1:
                    print('#')
                elif j == 0:
                    print('#', end='')
                elif j==x and i==y:
                    print('@', end='')    
                elif check_point(j,i):
                    print('0',end='')
                elif j==fx and i==fy:
                    print('F', end='')    
                              
                # ~ elif i == y and j == x and x==0:
                    # ~ print('X', end='')
                # ~ elif i == y and j == x and x==gameField_width:
                    # ~ print('X')
                # ~ elif i == y and j == x and y==0:
                    # ~ print('X', end='')
                # ~ elif i == y and j == x and y==gameField_height:
                    # ~ print('X', end='')
                else:
                    print(' ', end='')
    print('x =', x)
    print('y =', y)
    print('fx =', fx)
    print('fy =', fy)
    print(points)
    if state == END:
        print('Game over!')

def fruit():
    global fx,fy
    fx=random.randint(1,gameField_width-2)
    fy=random.randint(1,gameField_height-2)
        
def kb_handler():
    global direction
    if keyboard.is_pressed('Esc'):
        exit()
    elif keyboard.is_pressed('Up') and not direction == DOWN:
        direction = UP
    elif keyboard.is_pressed('Down') and not direction == UP:
        direction = DOWN
    elif keyboard.is_pressed('Left') and not direction == RIGHT:
        direction = LEFT
    elif keyboard.is_pressed('Right') and not direction == LEFT:
        direction = RIGHT
    
def exit_game():
    exit()
    
    
def main():
   
    global direction,state,x,y,fx,fy
    
    while True:
        kb_handler()
        if state == PLAY:
            # ~ move(direction)
            snake_move(direction)
            
        if fx == x and fy == y:
            snake_eat()
            fruit()
        draw()
        time.sleep(0.2)
        clear()
        
        
        
            

    # ~ time.sleep(0.2)
      

if __name__ == '__main__':
    main()
