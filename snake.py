import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Create display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by GitHub Coilot')

# Set clock
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Font style
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    paul_modran = {
        'game_over': False,
        'game_close': False,
        'x1': dis_width / 2,
        'y1': dis_height / 2,
        'x1_change': 0,
        'y1_change': 0,
        'snake_List': [],
        'Length_of_snake': 1,
        'foodx': round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
        'foody': round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    }

    while not paul_modran['game_over']:

        while paul_modran['game_close'] == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        paul_modran['game_over'] = True
                        paul_modran['game_close'] = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paul_modran['game_over'] = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paul_modran['x1_change'] = -snake_block
                    paul_modran['y1_change'] = 0
                elif event.key == pygame.K_RIGHT:
                    paul_modran['x1_change'] = snake_block
                    paul_modran['y1_change'] = 0
                elif event.key == pygame.K_UP:
                    paul_modran['y1_change'] = -snake_block
                    paul_modran['x1_change'] = 0
                elif event.key == pygame.K_DOWN:
                    paul_modran['y1_change'] = snake_block
                    paul_modran['x1_change'] = 0

        if paul_modran['x1'] >= dis_width or paul_modran['x1'] < 0 or paul_modran['y1'] >= dis_height or paul_modran['y1'] < 0:
            paul_modran['game_close'] = True
        paul_modran['x1'] += paul_modran['x1_change']
        paul_modran['y1'] += paul_modran['y1_change']
        dis.fill(white)
        pygame.draw.rect(dis, green, [paul_modran['foodx'], paul_modran['foody'], snake_block, snake_block])
        paul_modran['snake_List'].append([paul_modran['x1'], paul_modran['y1']])
        if len(paul_modran['snake_List']) > paul_modran['Length_of_snake']:
            del paul_modran['snake_List'][0]

        for x in paul_modran['snake_List'][:-1]:
            if x == [paul_modran['x1'], paul_modran['y1']]:
                paul_modran['game_close'] = True

        our_snake(snake_block, paul_modran['snake_List'])
        pygame.display.update()

        if paul_modran['x1'] == paul_modran['foodx'] and paul_modran['y1'] == paul_modran['foody']:
            paul_modran['foodx'] = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            paul_modran['foody'] = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            paul_modran['Length_of_snake'] += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()