import pygame, random
from pygame.locals import *

def randomico():
    x = random.randint(0,29)
    y = random.randint(0,29)

    return (x * pixel, y * pixel)

def hitApple(obj1, obj2):
    return (obj1[0] == obj2[0] and obj1[1] == obj2[1])

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('SnakeGame')

pixel = 20

snake_position = [(200,200),(220,200),(240,200)]
snake = pygame.Surface((pixel, pixel))
snake.fill((34,139,34))

apple_position = randomico()
apple = pygame.Surface((pixel, pixel)) 
apple.fill((255,0,0))

top = 0
down = 2
left = 3
direction = right = 1

font = pygame.font.Font('freesansbold.ttf', 20)
fps = pygame.time.Clock()
speed = 10
score = 0



while True:
    fps.tick(speed)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direction != down: direction = top
            elif event.key == K_LEFT and direction != right: direction = left
            elif event.key == K_RIGHT and direction != left: direction = right
            elif event.key == K_DOWN and direction != top: direction = down

    if hitApple(snake_position[0], apple_position):
        apple_position = randomico()
        snake_position.append((0,0))
        score += 1
        if score % 5 == 0: speed += 2

    if (
        snake_position[0][0] == screen.get_size()[0] 
        or snake_position[0][1] == screen.get_size()[1] 
        or snake_position[0][0] < 0 
        or snake_position[0][1] < 0
    ): break 

    for i in range(len(snake_position) -1):
        if snake_position[0][0] == snake_position[i][0] and snake_position[0][1] == snake_position[i][1]:
            break
        
    

    if direction == top: snake_position[0] = (snake_position[0][0], snake_position[0][1] - pixel)
    elif direction == down: snake_position[0] = (snake_position[0][0], snake_position[0][1] + pixel)
    elif direction == left: snake_position[0] = (snake_position[0][0] - pixel, snake_position[0][1])
    elif direction == right: snake_position[0] = (snake_position[0][0] + pixel, snake_position[0][1])

    for i in range(len(snake_position) - 1, 0, -1):
        snake_position[i] = (snake_position[i-1][0], snake_position[i-1][1])

    screen.fill((0,0,0))
    score_font = font.render('Sua pontuação: %s' %(score), True, (255,255,255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (400, 20)
    screen.blit(score_font, score_rect)
    screen.blit(apple, apple_position)

    for position in snake_position:
        screen.blit(snake, position)

    pygame.display.update()

while True: 
    perdeu_font = font = pygame.font.Font('freesansbold.ttf', 70)
    perdeu_screen = perdeu_font.render('Game Over', True, (255,255,255))
    perdeu_rect = perdeu_screen.get_rect()
    perdeu_rect.center = (300, 300)
    screen.blit(perdeu_screen, perdeu_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()