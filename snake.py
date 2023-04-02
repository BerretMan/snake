import pygame
from copy import deepcopy
class Snake:
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.case=[[10,9],[10,10]]
        self.screen = screen
        self.color=GREEN=(0,255,0)
        self.v_x =1
        self.v_y =0 
    def draw(self):
        for c in self.case:
           pygame.draw.rect(self.screen,self.color,(40*c[0],40*c[1],40,40)) 
    def move(self):
        l_case=deepcopy(self.case)
        self.case[-1][0] += self.v_x
        self.case[-1][1] += self.v_y
        for i in range(0,len(self.case)-1):
            self.case[i]= l_case[i+1]
    def growth(self):
        new_head=[self.case[-1][0]+self.v_x,self.case[-1][1]+self.v_y]
        self.case.append(new_head)
    
    def check_if_dead(self):
        #presence de double 
        if self.case[-1] in self.case[:-1] or 0>self.case[-1][0] or self.case[-1][0]>24 or self.case[-1][1]<0 or self.case[-1][1]>24:
            return True
        return False
    def coord(self):
        return self.case
            