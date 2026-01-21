import pygame as py

class SwitchingMrsCUNTiful(py.sprite.Sprite):
    def __init__(self,x,y,isPlayer2):
        super().__init__()
        self.image = py.Surface((350,350),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_1.png")
        self.img = py.transform.scale(self.img,(250,350))
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
        self.jumpy = y
        self.is_jump = False






    def Jump(self,pixalMove,DuckOccur,isPlayer2):
        if DuckOccur:
            self.rect.centery = 400
            
        if self.is_jump:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/jump.png")
            if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery -= pixalMove
            
        else:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/jump.png")
            if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(150,150)),self.image.get_rect())
            self.rect.centery += pixalMove



    def Duck(self,x,y,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/duck.png")
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(200,200)),self.image.get_rect())
        self.rect.centery = 550
        self.rect.centerx = x
        
        

    def DashBackCUNT(self,pixalMove,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        if isPlayer2:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/dash_back.png")
            self.img = py.transform.flip(self.img,True,False)
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(350,350)),self.image.get_rect())
            self.rect.centerx -= pixalMove
        else:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/dash_back.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(350,350)),self.image.get_rect())
            self.rect.centerx += pixalMove



    def DashForwardCUNT(self,pixalMove,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        if isPlayer2:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/dash_forward.png")
            self.img = py.transform.flip(self.img,True,False)
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(300,350)),self.image.get_rect())
            self.rect.centerx += pixalMove
        else:
            self.img = py.image.load("./CharSprites/MrsCUNTiful/dash_forward.png")
            self.image.fill((0,0,0,0))
            self.image.blit(py.transform.scale(self.img,(300,350)),self.image.get_rect())
            self.rect.centerx -= pixalMove
        


    # def Walkcycle(self,playerIdle,pixalMove,DuckOccur,JumpOccur,isPlayer2):
    #     if DuckOccur == True:
    #         self.rect.centery -= 150
    #     elif JumpOccur:
    #         self.rect.centery += 150
    #     self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_1.png")
    #     if isPlayer2:
    #         self.img = py.transform.flip(self.img,True,False)
    #     self.image.fill((0,0,0,0))
    #     self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
    #     self.rect.centerx += pixalMove
    #     self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_2.png")
    #     if isPlayer2:
    #         self.img = py.transform.flip(self.img,True,False)
    #     self.image.fill((0,0,0,0))
    #     self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
    #     self.rect.centerx += pixalMove
    #     self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_3.png")
    #     if isPlayer2:
    #         self.img = py.transform.flip(self.img,True,False)
    #     self.image.fill((0,0,0,0))
    #     self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
    #     self.rect.centerx += pixalMove
    #     self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle_frame_4.png")
    #     if isPlayer2:
    #         self.img = py.transform.flip(self.img,True,False)
    #     self.image.fill((0,0,0,0))
    #     self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
    #     self.rect.centerx += pixalMove



    def IdleCUNT(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/close_attack_idle.png")
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(200,350)),self.image.get_rect())
        

        #shooting long range
        #switch to chargeing for 0.3 and then use long range for 0.3 4 MrsCUNT

    def Block(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/block.png")
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    def Hit(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/being_hit.png")
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    def Attack(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/MrsCUNTiful/close_attack.png")
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.img = py.transform.rotate(self.img,90)
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(350,350)),self.image.get_rect())