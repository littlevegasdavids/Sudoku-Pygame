import pygame
import requests
from copy import deepcopy

#Constant Variables
DIFFICULTY = ['easy', 'medium', 'hard']
WIDTH = 550
BACKGROUND_COLOUR = (0,0,0)
LINE_COLOUR = (255, 255, 255)
NUM_COLOUR = (255, 255, 255)
BUFFER = 5

#Getting the values for the board based on the difficulty
response = requests.get("https://sugoku.herokuapp.com/board?difficulty={}".format(DIFFICULTY[0]))
grid_response = response.json()['board']

#Formatting the grid into a 2D array
grid = [[grid_response[x][y] for y in range(len(grid_response[0]))] for x in range(len(grid_response))]

#This is used to ensure that numbers from the board cannot be replaced by user
#Using deepcopy to make a copy of the instantiated grid instead of using grid_original as a reference for grid (this is how python variable assignments work)
grid_original = deepcopy(grid)

#Increment grid value by 1. If value == 9 then value == 0
def insert_mouse_pressed(window, myfont):
    pos = pygame.mouse.get_pos()
    x, y = pos[1]//50, pos[0]//50

    current_value = grid[x-1][y-1]
    if(current_value == 9):
        insert_value_block(window, 0, myfont)
    else:
        insert_value_block(window, current_value+1, myfont)

def insert_value_block(window, value, myfont):
    pos = pygame.mouse.get_pos()
    x, y = pos[1]//50, pos[0]//50

    if(value == 0 and grid_original[x-1][y-1] == 0):
        grid[x-1][y-1] = 0
        pygame.draw.rect(window, BACKGROUND_COLOUR, (y*50 + BUFFER, x*50+ BUFFER,50 -2*BUFFER , 50 - 2*BUFFER))
        pygame.display.update()

    #Condition to ensure that user does not replace a value that was given by the board
    elif(grid_original[x-1][y-1] == 0):
        grid[x-1][y-1] = value
        pygame.draw.rect(window, BACKGROUND_COLOUR, (y*50 + BUFFER, x*50+ BUFFER,50 -2*BUFFER , 50 - 2*BUFFER))
        value = myfont.render(str(value), True, NUM_COLOUR)
        window.blit(value, ((y*50)+18, (x*50)+15))
        pygame.display.update()
    return

def main():
    #Init the pygame window - setting width, title of window, icon and background colour
    pygame.init()
    window = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Sudoku')
    icon = pygame.image.load('logo.png')
    pygame.display.set_icon(icon)
    window.fill(BACKGROUND_COLOUR)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    #Drawing grid lines
    for i in range(0,10):
        if(i%3 == 0):
            #Drawing bolder lines to show grid boxes and outline of the grid
            pygame.draw.line(window, LINE_COLOUR, (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(window, LINE_COLOUR, (50, 50 + 50*i), (500, 50 + 50*i), 4)
        
        pygame.draw.line(window, LINE_COLOUR, (50 + 50*i, 50), (50 + 50*i ,500 ), 2)
        pygame.draw.line(window, LINE_COLOUR, (50, 50 + 50*i), (500, 50 + 50*i), 2)
    pygame.display.update()

    #Inserting values into grid
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, NUM_COLOUR)
                window.blit(value, (((j+1)*50) + 18, ((i+1)*50) + 15))
    pygame.display.update()

    #Infinite loop to keep window open and to listen to different events from the user
    while True:
        for event in pygame.event.get():
            #Mouse click in grid
            if(event.type == pygame.MOUSEBUTTONUP):
                if(event.button == 1):
                    pos = pygame.mouse.get_pos()
                    insert_mouse_pressed(window, myfont)
            
            #All keyboard presses for 0-9
            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_0 or event.key == pygame.K_KP0):
                    insert_value_block(window, 0, myfont)

                if(event.key == pygame.K_1 or event.key == pygame.K_KP1):
                    insert_value_block(window, 1, myfont)

                if(event.key == pygame.K_2 or event.key == pygame.K_KP2):
                    insert_value_block(window, 2, myfont)
                
                if(event.key == pygame.K_3 or event.key == pygame.K_KP3):
                    insert_value_block(window, 3, myfont)
                
                if(event.key == pygame.K_4 or event.key == pygame.K_KP4):
                    insert_value_block(window, 4, myfont)

                if(event.key == pygame.K_5 or event.key == pygame.K_KP5):
                    insert_value_block(window, 5, myfont)
                
                if(event.key == pygame.K_6 or event.key == pygame.K_KP6):
                    insert_value_block(window, 6, myfont)
                
                if(event.key == pygame.K_7 or event.key == pygame.K_KP7):
                    insert_value_block(window, 7, myfont)
                
                if(event.key == pygame.K_8 or event.key == pygame.K_KP8):
                    insert_value_block(window, 8, myfont)

                if(event.key == pygame.K_9 or event.key == pygame.K_KP9):
                    insert_value_block(window, 9, myfont)

            #Close the game
            if(event.type == pygame.QUIT):
                pygame.quit()

main()