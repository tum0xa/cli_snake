import os
import time
import random

import keyboard


DEBUG = False

# Settings

FPS = 10
GAME_FIELD = (80,25)

#Symbols
BORDER_SYM = '█'
FIELD_SYM = ' '
SNAKE_SYM = '▒'
HEAD_SYM = '░'
FRUIT_SYM = '▓'



SNAKE = 0
FRUIT = 1
HEAD = 1
GAME_STATE = 2
DIRECTION = 3


# EVENTS

LEFT = 10
RIGHT = 11
UP = 12
DOWN = 13

############

# Game state
GAME_NEW = 0
GAME_PLAY = 1
GAME_END = 2
GAME_START = 3
GAME_PAUSE = 4
GAME_EXIT = 5

############


if os.name == 'posix':
    clear = lambda: os.system('clear')
elif os.name == 'nt':
    clear = lambda: os.system('cls')
    
def game_init(game_field_dimensions=(80,25)):
    
    game_field_width = game_field_dimensions[0]
    game_field_height = game_field_dimensions[1]
    
    direction = RIGHT
    state = GAME_NEW

    fruit = fruit_new(game_field_dimensions)
    
    snake = [[3,int(game_field_height/2)],[2,int(game_field_height/2)],[1,int(game_field_height/2)]]
    return (snake, fruit, state, direction)
    


def check_point(point,points):
    
    if point in points:
        return True
    else:
        return False
        
def check_self_colision(snake):
    
    head = snake[0]
    if snake.count(head) > 1:
        return True
    else:
        return False
        
        
     
        
def snake_move(snake, direction):
        
    head = snake[0].copy()

    if direction == RIGHT:
        head[0] = head[0] + 1
    elif direction == LEFT:
        head[0] = head[0] - 1
    elif direction == UP:
        head[1] = head[1] - 1
    elif direction == DOWN:
        head[1] = head[1] + 1
    else:
        return snake
        
    snake.insert(0,head)
    snake.pop()
    
    return snake
    


def snake_eat(snake,fruit_pos):
    
    fruit_x = fruit_pos[0]
    fruit_y = fruit_pos[1]
    
    snake.insert(0,[fruit_x,fruit_y])
    
    return snake

def draw(snake, head_pos, fruit_pos, game_field_dimensions=(80,25),
    game_field_sym=' ', snake_sym='*', fruit_sym='F', border_sym='#', 
    head_sym='@',game_message=''):

    
    game_field_width = game_field_dimensions[0]
    game_field_height = game_field_dimensions[1]
    
    head_x = head_pos[0]
    head_y = head_pos[1]
    
    fruit_x = fruit_pos[0]
    fruit_y = fruit_pos[1]
    
    
    for i in range(game_field_height):
        for j in range(game_field_width):
            # Draw the game field borders ########
            if i == 0 or i == game_field_height-1: # Vertical borders
                if j == game_field_width-1: # Right border
                    print(border_sym)
                else:                       # Left border
                    print(border_sym, end='')
            else:                                  # Horizontal borders
                if j == game_field_width-1: # Bottom border
                    print(border_sym)
                elif j == 0:                # Top border
                    print(border_sym, end='')
            ##### End draw borders################
            
            # Draw snake's head ##################
                elif j==head_x and i==head_y:
                    print(head_sym, end='')    
            ##### End draw snake's head###########
            
            # Draw snake's body ##################
                elif check_point([j,i], snake):
                    print(snake_sym,end='')
            ##### End draw snake's body ##########
            
            # Draw fruit #########################        
                elif j==fruit_x and i==fruit_y:
                    print(fruit_sym, end='')      
            ##### End draw fruit #################
            
            # Fill the game field ################
                else:
                    print(game_field_sym, end='')
            
            ##### End fill the game field ########
                    
    # Draw the game message
    if game_message:
        print(game_message)
        
        
    if DEBUG == True:
        
        print('head x =', head_x)
        print('head y =', head_y)
        print('fruit x =', fruit_x)
        print('fruit y =', fruit_y)
        print(snake)  
        

def fruit_new(game_field_dimensions=(80,25)):
    
    game_field_width = game_field_dimensions[0]
    game_field_height = game_field_dimensions[1]
    
    fruit_x=random.randint(1,game_field_width-2)
    fruit_y=random.randint(1,game_field_height-2)
    
    return (fruit_x,fruit_y)
        
        
def kb_handler():
    
    if keyboard.is_pressed('Esc'):
        event = GAME_EXIT
    elif keyboard.is_pressed('Up'):
        event = UP
    elif keyboard.is_pressed('Down'):
        event = DOWN
    elif keyboard.is_pressed('Left'):
        event = LEFT
    elif keyboard.is_pressed('Right'):
        event = RIGHT
    elif keyboard.is_pressed('Enter'):
        event = GAME_START
    elif keyboard.is_pressed('Space'):
        event = GAME_PAUSE
    else:
        event = GAME_PLAY
    return event
        
    
def exit_game():
    exit()
    
    
def main():
    old_delta = 0
    new_fruit = 0 
    new_game = game_init(GAME_FIELD)
    game_field_width = GAME_FIELD[0]
    game_field_height = GAME_FIELD[1]
    fruit_time = 200
    snake = new_game[SNAKE]
    # ~ print(snake)
    head = snake[0]
    fruit = new_game[FRUIT]
    old_snake = len(snake)
    game_state = new_game[GAME_STATE]
    direction = new_game[DIRECTION]

    message = 'Welcome to the Snake! Press Enter to start new game!'
    
    while True:
        new_fruit+=1
        time_start = time.time()
        event = kb_handler() # Keyboard handler
        fruit_x = fruit[0]
        fruit_y = fruit[1]
        if game_state == GAME_NEW:
            
            if event == GAME_START:
                game_state = GAME_PLAY
            elif event == GAME_EXIT:
                game_state = GAME_EXIT
        
        elif game_state == GAME_PAUSE:
            
            if event == GAME_START:
                game_state = GAME_PLAY
                
            elif event == GAME_EXIT:
                game_state = GAME_EXIT
                
            elif event == GAME_PAUSE:
                game_state = GAME_PLAY
                event = GAME_START
            
        
        elif game_state == GAME_PLAY:
            message='Ponts: '+str(len(snake)*10-30)
            if event == UP and not direction == DOWN:
                direction = UP
            elif event == DOWN  and not direction == UP:
                direction = DOWN
            elif event == LEFT  and not direction == RIGHT:
                direction = LEFT
            elif event == RIGHT  and not direction == LEFT:
                direction = RIGHT
            
                
            if event == GAME_PAUSE:
                game_state = GAME_PAUSE
                message = 'Game paused'
                
            elif event == GAME_EXIT:
                game_state = GAME_EXIT
                message = 'Thank you for a game!'
            else:
                            
                snake = snake_move(snake,direction)
                
                head = snake[0]
                head_x = head[0]
                head_y = head[1]
                
                if check_self_colision(snake):
                    game_state = GAME_END
                    
                # ~ if direction == RIGHT and head_x+1 == fruit_x and head_y == fruit_y \
                    # ~ or direction == LEFT and head_x-1 == fruit_x and head_y == fruit_y \
                    # ~ or direction == UP and head_y-1 == fruit_y and head_x == fruit_x \
                    # ~ or direction == DOWN and head_y+1 == fruit_y and head_x == fruit_x:
                if head_x == fruit_x and head_y == fruit_y:
                    
                    snake = snake_eat(snake,fruit)
                    fruit = fruit_new(GAME_FIELD)
                    new_fruit = 0
                    
                if new_fruit == fruit_time:
                    fruit = fruit_new(GAME_FIELD)
                    
                if len(snake) == old_snake+3:
                    fruit_time -= 20
                    old_snake = len(snake)
                    if fruit_time == 20:
                        fruit_time = 20
                
                elif head_x > game_field_width-2:
                    head_x = game_field_width-2
                    game_state = GAME_END
                elif head_x < 1:
                    head_x = 1
                    game_state = GAME_END
                if head_y > game_field_height-2:
                    head_y = game_field_height-2
                    game_state = GAME_END
                elif head_y < 1:
                    head_y = 1
                    game_state = GAME_END         
            
        elif game_state == GAME_END:
            message = 'Game over! Your result is ' + str(len(snake)*10-30) + '. Press "Enter" to start new game or "Esc" to exit.'
            if event == GAME_START:
                del new_game, head, head_x, head_y, snake, fruit, fruit_x, fruit_y, game_state, direction
                new_game = game_init(GAME_FIELD)
                
                snake = new_game[SNAKE]
                head = snake[0]
                fruit = new_game[FRUIT]
                fruit_x = fruit[0]
                fruit_y = fruit[1]
                
                direction = new_game[DIRECTION]
                game_state = GAME_PLAY   
                
            if event == GAME_EXIT:
                game_state = GAME_EXIT    
        elif game_state == GAME_EXIT:
            exit()

        clear()
        draw(snake, head, fruit, game_field_dimensions=GAME_FIELD, game_message=message,
        border_sym=BORDER_SYM, snake_sym=SNAKE_SYM, game_field_sym=FIELD_SYM, 
        fruit_sym=FRUIT_SYM, head_sym=HEAD_SYM)
        time_end = time.time()
        delta = time_end - time_start
        # ~ print(delta)
        # ~ print(1/FPS-delta)
        # ~ print(old_delta)
        time.sleep(abs(1/FPS-delta))   
        time_end = time.time()
        old_delta = time_end - time_start
        


if __name__ == '__main__':
    main()
    
