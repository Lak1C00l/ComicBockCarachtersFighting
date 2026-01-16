import pygame as py

class SwitchingMrsCUNTiful(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((250,350),py.SRCALPHA)
        self.rect = self.image.get_rect()
        
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_1.png")
        self.img = py.transform.scale(self.img,(250,350))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y

    def Jump(self,x,y,pixalMove):
        self.rect.centerx = x
        self.rect.centery = y
        for i in range(11):
            self.rect.centery += pixalMove
            self.img = py.transform.scale(self.img,(100,100))
            self.image.blit(self.img,self.rect)

        for i in range(11):
            self.rect.centery -= pixalMove
            self.img = py.transform.scale(self.img,(100,100))
            self.image.blit(self.img,self.rect)

    def Duck(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y
        self.img = py.image.load("./CharSprites/MrsCUNTiful/duck")
        self.img = py.transform.scale(self.img,(250,350))
        self.image.blit(self.img,self.rect)


    def DashForward(self,x,y,pixalMove):
        
        #change apperance of sprite
        #self.image = py.Surface((100,100),py.SRCALPHA)
        #get rect of sprite being used
        #self.image = py.Surface((100,100),py.SRCALPHA)
        #self.image.fill((0,0,0,0))
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_2.png")
        self.img = py.transform.scale(self.img,(250,350))
        # self.rect = self.image.get_rect()
        # self.rect.centerx = x
        # self.rect.centery = y
        self.image.blit(self.img,self.rect)
        # while key is pressed keep dashing
        self.rect.centerx += pixalMove

    def DashBack(self,x,y,pixalMove):
        self.rect.centerx = x
        self.rect.centery = y
        #change apperance of sprite
        #self.image = py.Surface((100,100),py.SRCALPHA)
        #self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_3.png")
        self.img = py.transform.scale(self.img,(250,350))
        self.image.blit(self.img,self.rect)

        # while key is pressed keep dashing
        self.rect.centerx -= pixalMove
    def Walkcycle(self,x,y,playerIdle):
        self.rect.centerx = x
        self.rect.centery = y

    

