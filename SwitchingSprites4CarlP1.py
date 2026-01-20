import pygame as py

class SwitchingCarl(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((300,350),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Carl/without_backround/walk_cycle/walk_cycle_frame_1.png")
        self.img = py.transform.scale(self.img,(150,350))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
        self.jumpy = y
        self.is_jump = False

    def Jump(self,pixalMove,DuckOccur):
        if DuckOccur:
            self.rect.centery = 450
        if self.is_jump:
            self.img = py.image.load("./CharSprites/Carl/without_backround/jump.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery -= pixalMove
            
        else:
            self.img = py.image.load("./CharSprites/Carl/without_backround/jump.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery += pixalMove


    def Duck(self,x,y,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 450
        x = self.rect.centerx
        y = self.rect.centery
        self.img = py.image.load("./CharSprites/Carl/without_backround/duck.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(200,200)),self.image.get_rect())
        self.rect.centery = y + 150
        self.rect.centerx = x


    def DashBackCarl(self,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 450
        self.img = py.image.load("./CharSprites/Carl/without_backround/dash_back.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx -= pixalMove
    
    def DashForwardCarl(self,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 450
        self.img = py.image.load("./CharSprites/Carl/without_backround/dash_forwards.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(350,350)),self.image.get_rect())
        self.rect.centerx += pixalMove

        
    def Walkcycle(self,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur == True:
            self.rect.centery -= 150
        elif JumpOccur:
            self.rect.centery += 150
        self.img = py.image.load("./CharSprites/Carl/without_backround/walk_cycle_frame_1.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove

        self.img = py.image.load("./CharSprites/Carl/without_backround/walk_cycle_frame_2.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove

        self.img = py.image.load("./CharSprites/Carl/without_backround/walk_cycle_frame_3.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove

        self.img = py.image.load("./CharSprites/Carl/without_backround/walk_cycle_frame_4.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx += pixalMove



    def IdleCarl(self,DuckOccur,JumpOccur):
        if DuckOccur == True:
            self.rect.centery -= 150
        elif JumpOccur:
            self.rect.centery += 150
        self.img = py.image.load("./CharSprites/Carl/without_Backround/close_attack_idle.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
   
    def Block(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 450
        self.img = py.image.load("./CharSprites/Carl/without_backround/block.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    def Hit(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 450
        self.img = py.image.load("./CharSprites/Carl/without_backround/being_hit.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())