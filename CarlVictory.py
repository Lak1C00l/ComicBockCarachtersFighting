
"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task

Date Modified: Thursday, January 22nd, 2026
"""

import pygame as py

"""
The CarlVictoryPose Class draws Carl's victory pose to the screen 
"""
class CarlVictoryPose(py.sprite.Sprite):
    """
    The initalize function takes in x and y coordinate and uses them to draw the sprite at the correct position
    """
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((550,800),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Carl/without_backround/victoryPose.png")
        self.img = py.transform.scale(self.img,(550,800))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y