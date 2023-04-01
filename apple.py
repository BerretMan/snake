from random import randint
import pygame
class Apple:
    def __init__(self,screen):
        self.n_case=24
        self.x = randint(0,self.n_case)
        self.y = randint(0,self.n_case)
        self.screen = screen
        self.color =  (255,0,0)
    
    def draw(self):
        pygame.draw.rect(self.screen,self.color,(40*self.x,40*self.y,40,40)) 
    def gen_new_apple(self):
        self.x = randint(0,self.n_case)
        self.y = randint(0,self.n_case)

    