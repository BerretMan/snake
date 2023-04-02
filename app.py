import pygame, sys
from pygame.locals import *
from snake import Snake 
from apple import Apple
from brain import Brain
GENERATION=0
INDIVIDU=0
INDIVIDU_PAR_GEN=100
SPEED=1
score = 0
pygame.init()
screen = pygame.display.set_mode((1000, 1000), 0 , 32)
pygame.display.set_caption(f'Snake, by BerretMan, score={score},INDIVIDU={INDIVIDU},GENERATION={GENERATION}')

BLACK = (0,0,0)
player = Snake(screen)
apple=Apple(screen)
clock = pygame.time.Clock()

list_brain= [Brain(player,apple) for _ in range(INDIVIDU_PAR_GEN+1)]
fitness_list=[[None,None]]*INDIVIDU_PAR_GEN
TEMPS_SURVIE=0
while True:
    if SPEED==1:
        clock.tick(720)
    if SPEED==0:
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
            if event.key == pygame.K_o:
                SPEED=1
            if event.key == pygame.K_p:
                SPEED=0
            if event.key == pygame.K_y:
                INDIVIDU+=1
                fitness_list[INDIVIDU]=-1
                
    if player.case[-1][0] == apple.x and player.case[-1][1] == apple.y:
        apple.gen_new_apple()
        player.growth()
        score +=1
        pygame.display.set_caption(f'Snake, by BerretMan, score={score},INDIVIDU={INDIVIDU},GENERATION={GENERATION}')
    else:
        player.move()
    if player.check_if_dead():
        if INDIVIDU==INDIVIDU_PAR_GEN: # reproduction
            print(f"gen {GENERATION}")
            # print(fitness_list)
            fitness_list.sort(key=lambda tup: tup[1], reverse=True)
            print(fitness_list[:10])
            # premier
            list_brain[0]= list_brain[fitness_list[0][0]]
            # 5 suivants
            for x in range(1,10):
                individus =Brain(player,apple)
                individus.poid=[(g+h)/2 for g,h in zip(list_brain[0].poid,list_brain[fitness_list[x][0]].poid)]
                list_brain[x] = individus
            for x in range(10,INDIVIDU_PAR_GEN):
                list_brain[x] = Brain(player,apple)

            INDIVIDU=0
            GENERATION+=1
        fitness_list[INDIVIDU]=[INDIVIDU,score+TEMPS_SURVIE/100]
        TEMPS_SURVIE=0
        score=0
        INDIVIDU+=1
        player = Snake(screen)
        apple=Apple(screen)
        pygame.display.set_caption(f'Snake, by BerretMan, score={score},INDIVIDU={INDIVIDU},GENERATION={GENERATION}')
    list_brain[INDIVIDU].player=player
    list_brain[INDIVIDU].apple=apple
    list_brain[INDIVIDU].get_entry()
    list_brain[INDIVIDU].play()
    TEMPS_SURVIE+=1
    player.draw()
    apple.draw()
    pygame.display.update()
    screen.fill(BLACK)
