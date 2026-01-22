import pygame as py

class SwitchingKisha(py.sprite.Sprite):
    def __init__(self,x,y,isPlayer2):
        super().__init__()
        self.image = py.Surface((350,400),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Kisha/with_backround/walk_cycle/walk_frame_1.png")
        self.img = py.transform.scale(self.img,(250,400))
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
        self.jumpy = y
        self.is_jump = False

    



    def Jump(self,pixalMove,DuckOccur,isPlayer2):
        if DuckOccur:
            self.rect.centery = 375
        if self.is_jump:
            self.img = py.image.load("./CharSprites/Kisha/without_backround/jump.png")
            self.image.fill((0,0,0,0))
            if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
            self.image.blit(py.transform.scale(self.img,(250,200)),self.image.get_rect())
            self.rect.centery -= pixalMove
            
        else:
            self.img = py.image.load("./CharSprites/Kisha/without_backround/jump.png")
            self.image.fill((0,0,0,0))
            if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
            self.image.blit(py.transform.scale(self.img,(250,200)),self.image.get_rect())
            self.rect.centery += pixalMove



    def Duck(self,x,y,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        x = self.rect.centerx
        y = self.rect.centery
        self.img = py.image.load("./CharSprites/Kisha/without_backround/duck.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(300,300)),self.image.get_rect())
        self.rect.centery = 500


    def DashBackKisha(self,pixalMove,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        if isPlayer2:
            self.img = py.image.load("./CharSprites/Kisha/without_backround/dash_back.png")
            self.image.fill((0,0,0,0))
            self.img = py.transform.flip(self.img,True,False)
            self.image.blit(py.transform.scale(self.img,(350,400)),self.image.get_rect())
            self.rect.centerx += pixalMove
        else:
            self.img = py.image.load("./CharSprites/Kisha/without_backround/dash_back.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(350,400)),self.image.get_rect())
            self.rect.centerx -= pixalMove
    


    def DashForwardKisha(self,pixalMove,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        if isPlayer2:
            self.img = py.image.load("./CharSprites/Kisha/without_backround/dash_forward.png")
            self.image.fill((0,0,0,0))
            self.img = py.transform.flip(self.img,True,False)
            self.image.blit(py.transform.scale(self.img,(350,400)),self.image.get_rect())
            self.rect.centerx -= pixalMove
        else:
            self.img = py.image.load("./CharSprites/Kisha/without_backround/dash_forward.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(350,400)),self.image.get_rect())
            self.rect.centerx += pixalMove


    def IdleKisha(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_Backround/close_attack_idle.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    def Attack(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_Backround/close_attack_left.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(300,400)),self.image.get_rect())


    def Block(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_backround/block.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(250,400)),self.image.get_rect())

    def Hit(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_backround/being_hit.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(350,400)),self.image.get_rect())