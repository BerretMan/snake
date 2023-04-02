#réseau de neuronne 6 entry 
#24 poids
#4 output
from random import uniform 

class Brain:
    def __init__(self,player,apple):
        self.n_entry = 6
        self.n_poid = 130
        self.n_output = 4
        self.player=player #l'objet
        self.apple=apple
        self.entry=self.get_entry()
        self.poid= [uniform(0, 1) for _ in range(self.n_poid)]
        self.fitness=0
    def get_entry(self):
        #distance mur g d haut bas
        d_g_w=self.player.case[-1][0]
        d_d_w=24-self.player.case[-1][0]
        d_h_w=self.player.case[-1][1]
        d_b_w=24-self.player.case[-1][1]
        
        # distance pomme g d haut bas
        d_x_p=self.player.case[-1][0]-self.apple.x
        d_y_p=self.player.case[-1][1]-self.apple.y
        self.entry= [d_g_w,d_d_w,d_h_w,d_b_w,d_x_p,d_y_p]
    def get_coord(self):
        return self.player.coord()
    def play(self):
        couche_1=[sum(entry*poid for (entry,poid) in zip(self.entry,self.poid[(x-1)*0:x*6]))/36 for x in range(1,96)]
        z=sum(c1*poid for (c1,poid) in zip(couche_1,self.poid[97:105]))
        q=sum(entry*poid for (entry,poid) in zip(self.entry,self.poid[105:113]))/32
        s=sum(entry*poid for (entry,poid) in zip(self.entry,self.poid[113:121]))/32
        d=sum(entry*poid for (entry,poid) in zip(self.entry,self.poid[121:129]))/32
        if z > 0.4 and self.player.v_y !=1:
            self.player.v_x=0
            self.player.v_y=-1
            return None 
        if s > 0.4 and self.player.v_y !=-1:
            self.player.v_x=0
            self.player.v_y=1
            return None 
        if q > 0.4 and self.player.v_x !=1:
            self.player.v_x=-1
            self.player.v_y=0
            return None 
        if d > 0.4 and self.player.v_x !=-1:
            self.player.v_x=1
            self.player.v_y=0
            return None 