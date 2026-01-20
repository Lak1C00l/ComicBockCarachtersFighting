import pygame as py
from time import sleep

class SwitchingMrsCUNTiful(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((350,350),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_1.png")
        self.img = py.transform.scale(self.img,(250,350))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
        self.jumpy = y
        self.is_jump = False






    def Jump(self,pixalMove,DuckOccur):
        if DuckOccur:
            self.rect.centery = 400
            
        if self.is_jump:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/jump.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery -= pixalMove
            
        else:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/jump.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery += pixalMove



    def Duck(self,x,y,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        x = self.rect.centerx
        y = self.rect.centery
        self.img = py.image.load("./CharSprites/MrsCUNTiful/duck.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(200,200)),self.image.get_rect())
        self.rect.centery = y + 150
        self.rect.centerx = x
        
        

    def DashBackCUNT(self,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/dash_back.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(350,350)),self.image.get_rect())
        self.rect.centerx -= pixalMove

        
        
    def Walkcycle(self,playerIdle,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur == True:
            self.rect.centery -= 150
        elif JumpOccur:
            self.rect.centery += 150
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_1.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_2.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_3.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_4.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove


    def DashForwardCUNT(self,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/dash_forward.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove
    


    def IdleCUNT(self,DuckOccur,JumpOccur):
        if DuckOccur == True:
            self.rect.centery -= 150
        elif JumpOccur:
            self.rect.centery += 150
        self.img = py.image.load("./CharSprites/MrsCUNTiful/close_attack_idle.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

        #shooting long range
        #switch to chargeing for 0.3 and then use long range for 0.3 4 MrsCUNT

    def Block(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/block.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    def Hit(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/being_hit.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    def Attack(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/close_attack.png")
        py.transform.rotate(self.img,90)
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,400)),self.image.get_rect())