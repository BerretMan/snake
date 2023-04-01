import pygame, sys
from pygame.locals import *
from snake import Snake 
from apple import Apple
pygame.init()
screen = pygame.display.set_mode((1000, 1000), 0 , 32)
pygame.display.set_caption('Snake, by BerretMan, score=0')

BLACK = (0,0,0)
player = Snake(screen)
apple=Apple(screen)
clock = pygame.time.Clock()
score = 0 
while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and player.v_y !=-1:
                player.v_x=0
                player.v_y=1
            if event.key == pygame.K_z and player.v_y !=1:
                player.v_x=0
                player.v_y=-1
            if event.key == pygame.K_q and player.v_x !=1:
                player.v_x=-1
                player.v_y=0
            if event.key == pygame.K_d and player.v_x !=-1:
                player.v_x=1
                player.v_y=0
    if player.case[-1][0] == apple.x and player.case[-1][1] == apple.y:
        apple.gen_new_apple()
        player.growth()
        score +=1
        pygame.display.set_caption(f'Snake, by BerretMan, score={score}')
    else:
        player.move()
    if player.check_if_dead():
        pygame.quit()
        print("game over, ton score est de", score)
        sys.exit()
    player.draw()
    apple.draw()
    pygame.display.update()
    screen.fill(BLACK)
