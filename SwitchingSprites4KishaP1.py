"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task

Date Modified: Thursday, January 22nd, 2026
"""

import pygame as py

class SwitchingKisha(py.sprite.Sprite):
    def __init__(self,x,y,isPlayer2):
        super().__init__()
        self.image = py.Surface((350,400),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Kisha/without_backround/close_attack_idle.png")
        self.img = py.transform.scale(self.img,(300,400))
        if isPlayer2:
            self.img = py.transform.flip(self.img,True,False)
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
        self.jumpy = y
        self.is_jump = False

    


    """
    The Jump function changes Kisha's image to be in the ducking position and it moves Kisha up along the y axis and the back down 
    along that y axis to create a full jump. It dose this by taking in how many pixals it should move by and if before this a duck 
    has already occured. If the move before this was a Duck than it resets the centery value to 400 so the jump always takes place at 
    the same height. Then if Kisha is currently jumping aka self.jumpy is True it uses the value of pixalMove to move Kisha up 
    by that speed. If Kisha is not currently jumping than it uses pixalMove to move Kisha back downwards to the starting point aka when it's
    centery is 400. It also takes in isPlayer2 to flip the image every time it is redrawn.
    """
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


    """
    The Duck function changes the image of Kisha's sprite to the ducking position and put's the sprites centery value to 375
    so it appears lower down on the screen. It also takes in isPlayer2 to flip the image every time it is redrawn.
    """
    def Duck(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_backround/duck.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(300,300)),self.image.get_rect())
        self.rect.centery = 500

    """
    The DashBackKisha function changes the image of the sprite to dashing back and moves it to the right by using pixalMove
    to know at which speed to move Kisha. It also takes in DuckOccur and JumpOccur to know if that was the movemnt that
    happened before this one. If so, then it sets the centery back to 400 so the sprite image appears at the correct spot.
    It also takes in isPlayer2 to flip the image every time it is redrawn.
    """
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
    

    """
    The DashForwardKisha function changes the image of the sprite to dashing back and moves it to the left by using pixalMove
    to know at which speed to move Kisha. It also takes in DuckOccur and JumpOccur to know if that was the movemnt that
    happened before this one. If so, then it sets the centery back to 400 so the sprite image appears at the correct spot.
    It also takes in isPlayer2 to flip the image every time it is redrawn.
    """
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


    """
    The Attack function changes Kisha's sprite to her attack image, it also takes in DuckOccur and JumpOccur, if either evaluates
    to true then the centery is changes to 375 so the sprite is drawn at the correct position, otherwise it will draw the sprite 
    to low or too high. It also takes in isPlayer2 to flip the image every time it is redrawn.
    """
    def Attack(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_Backround/close_attack_left.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(300,400)),self.image.get_rect())


    """
    The block function changes Kisha's sprite to her blocking image, it also takes in DuckOccur and JumpOccur, if either evaluates
    to true then the centery changes to 375(the center of all standing sprites) so the sprite is drawn at the correct position, otherwise it will draw the sprite 
    to low or too high. It also takes in isPlayer2 to flip the image every time it is redrawn.
    """
    def Block(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_backround/block.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(250,400)),self.image.get_rect())

    """
    The Hit function changes Kisha's sprite to her being hit pose, it also takes in DuckOccur and JumpOccur, if either evaluates
    to true then the centery is changed to 375 so the sprite is drawn at the correct position, otherwise it will draw the sprite 
    to low or too high. It also takes in isPlayer2 to flip the image every time it is redrawn.
    """
    def Hit(self,DuckOccur,JumpOccur,isPlayer2):
        if DuckOccur or JumpOccur:
            self.rect.centery = 375
        self.img = py.image.load("./CharSprites/Kisha/without_backround/being_hit.png")
        self.image.fill((0,0,0,0))
        if isPlayer2:
                self.img = py.transform.flip(self.img,True,False)
        self.image.blit(py.transform.scale(self.img,(350,400)),self.image.get_rect())