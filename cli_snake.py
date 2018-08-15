import os
import time
import random

import keyboard

global x, y, direction, state, fx,fy, snake

gameField_width = 40
gameField_height = 20

DEBUG = True

# Directions

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

############

# Game state

PLAY = 0
END = 1

############


if os.name == 'posix':
    clear = lambda: os.system('clear')
elif os.name == 'nt':
    clear = lambda: os.system('cls')
    
def game_init():
    global x, y, direction, state, fx,fy, snake
    
    x = 4
    y = 1
    
    direction = RIGHT
    state = PLAY

    fruit()
    
    snake = [[3,2],[2,1],[1,1]]
    


def check_point(pointx,pointy):
    global snake
    point = [pointx,pointy]
    if point in snake:
        return True
    else:
        return False
        
def check_colision():
    global snake,state,head
    
    for point in snake:
        if snake.count(head) > 1:
            state = END
        
        
     
        
def snake_move(direction):
    global snake, x, y, state,head
    
    head = snake[0].copy()

    if direction == RIGHT:
        head[0] = head[0] + 1
    elif direction == LEFT:
        head[0] = head[0] - 1
    elif direction == UP:
        head[1] = head[1] - 1
    elif direction == DOWN:
        head[1] = head[1] + 1

    snake.insert(0,head)
    snake.pop()
    x = head[0]
    y = head[1]


def snake_eat():
    global snake,fx,fy
    snake.insert(0,[fx,fy])

def draw(message):
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
                else:
                    print(' ', end='')
    if message:
        print(message)
        
        
    if DEBUG == True:
        print('x =', x)
        print('y =', y)
        print('fx =', fx)
        print('fy =', fy)
        print(snake)  
        

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
    elif keyboard.is_pressed('Enter'):
        game_init()
        
    
def exit_game():
    exit()
    
    
def main():
   
    global direction,state,x,y,fx,fy
    
    game_init()
    old_length=len(snake)
    
    message=''
    while True:
        kb_handler() # Keyboard handler
        
        if state == PLAY:
            snake_move(direction)
            check_colision()
    
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
        
        if state == END:
            message = 'Game over! Press "Enter" to start new game or "Esc" to exit.'
           
        
        if fx == x and fy == y:
            snake_eat()
            fruit()

        clear()
        draw(message)
              
        time.sleep(0.1)   


if __name__ == '__main__':
    main()
