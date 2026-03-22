"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task

Date Modified: Thursday, January 22nd, 2026
"""

import pygame as py
"""
The class Switching Carl switches the displayed sprite for Carl to another image and can move him depending on which function is called
"""
class SwitchingCarl(py.sprite.Sprite):
    """
    The init function draws the idle pose that appears onscreen when you first open the program, by using the x and y inputs it draws
    this sprite to the screen at those coordinates. 
    """
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((300,350),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Carl/without_backround/short_range_aiming.png")
        self.img = py.transform.scale(self.img,(250,350))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
        self.jumpy = y
        self.is_jump = False



    """
    The Jump function changes Carl's image to be in the ducking position and it moves Carl up along the y axis and the back down 
    along that y axis to create a full jump. It dose this by taking in how many pixals it should move by and if before this a duck 
    has occured. If the move before this was a Duck than it resets the centery value to 400 so the jump always takes place at 
    the same height. Then if Carl is currently jumping aka self.jumpy is True it uses the value of pixalMove to move Carl up 
    by that speed. If Carl is not currently jumping than it uses pixalMove to move Carl back downwards to the starting point aka when it's
    centery is 400.
    """
    def Jump(self,pixalMove,DuckOccur):
        if DuckOccur:
            self.rect.centery = 400
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

    """
    The Duck function changes the image of Carl's sprite to the ducking position and put's the sprites centery value to 550
    so it appears lower down on the screen.
    """
    def Duck(self):
        self.img = py.image.load("./CharSprites/Carl/without_backround/duck.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(200,200)),self.image.get_rect())
        self.rect.centery = 550

    """
    The DashBackCarl function changes the image of the sprite to dashing back and moves it to the left by using pixalMove
    to know at which speed to move Carl. It also takes in DuckOccur and JumpOccur to know if that was the movemnt that
    happened before this one. If so, then it sets the centery back to 400 so the sprite image appears at the correct spot.
    """
    def DashBackCarl(self,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/Carl/without_backround/dash_back.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())
        self.rect.centerx -= pixalMove
    
    """
    The DashForwardCarl function changes the image of Carl's sprite to dashing back and it moves it to the right by using pixalMove
    to know at which speed to move Carl. It also takes in DuckOccur and JumpOccur to know if that was the movemnt that
    happened before this one. If so, then it sets the centery value back to 400 so the sprite image appears at the correct spot.
    """
    def DashForwardCarl(self,pixalMove,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400

        self.img = py.image.load("./CharSprites/Carl/without_backround/dash_forwards.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(350,350)),self.image.get_rect())
        self.rect.centerx += pixalMove

    """
    The Block function changes Carl's sprite image to his blocking pose and it takes in DuckOccur and JumpOccur as to change the centery
    value of Carl's sprite back to 400 if either is true so the image appears at the correct spot. 
    """
    def Block(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/Carl/without_backround/block.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    """
    The Hit function changes Carl's sprite image to his being hit pose and it takes in DuckOccur and JumpOccur as to change the centery
    value of Carl's sprite back to 400 if either is true so the image appears at the correct spot. 
    """
    def Hit(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/Carl/without_backround/being_hit.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())

    """
    The Attack function changes Carl's sprite image to his attacking pose and it takes in DuckOccur and JumpOccur as to change the centery
    value of Carl's sprite back to 400 if either is true so the image appears at the correct spot. 
    """
    def Attack(self,DuckOccur,JumpOccur):
        if DuckOccur or JumpOccur:
            self.rect.centery = 400
        self.img = py.image.load("./CharSprites/Carl/without_backround/punch_with_left.png")
        self.image.fill((0,0,0,0))
        self.image.blit(py.transform.scale(self.img,(250,350)),self.image.get_rect())