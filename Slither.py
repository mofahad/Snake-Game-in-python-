import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0,0,255)
dd = (24,54,55)
df = (62,36,45,0)
yellow = (255,255,0)
df = (0,255,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SnakeGame')

clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont("Times New Roman", 25,bold=True)


def snake(block_size, snakelist):
    for XnY in snakelist:
        #pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], 35, 35])
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[200,80])


def gameLoop():

    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0


    snakeList = []
    snakeLength = 20

    randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(dd)
            message_to_screen("Game over, press P to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(dd)

        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]


        snake(block_size, snakeList)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            snakeLength+= 1
        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()

