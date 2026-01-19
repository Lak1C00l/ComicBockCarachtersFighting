import pygame as py

class SwitchingKisha(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((250,350),py.SRCALPHA)
        self.rect = self.image.get_rect()
        
        self.img = py.image.load("./CharSprites/Kis_/walk_cycle/walk_cycle_frame_1.png")
        self.img = py.transform.scale(self.img,(250,350))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y

    def Jump(self,pixalMove):
        for i in range(11):
            self.img = py.image.load("./CharSprites/Kis_/jump.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery += pixalMove
            
        for i in range(11):
            self.img = py.image.load("./CharSprites/Kisha/with_backround/jump.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery -= pixalMove
            
            

    def Duck(self,x,y):
        # self.rect.centerx = x - 100
        #self.rect.centery = y + 100
        self.img = py.image.load("./CharSprites/Kis_/duck.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())


    def DashBackCUNT(self,pixalMove):
        self.img = py.image.load("./CharSprites/Kis_/dash_back.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(350,350)),self.image.get_rect())

        self.rect.centerx -= pixalMove

        # while key is pressed keep dashing
        self.rect.centerx -= pixalMove
    def Walkcycle(self,playerIdle):
        pluh = 1

    def DashForwardCUNT(self,pixalMove):
        self.img = py.image.load("./CharSprites/Kis_/dash_forward.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

        self.rect.centerx += pixalMove