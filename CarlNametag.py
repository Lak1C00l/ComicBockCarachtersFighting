"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task

Date Modified: Thursday, January 22nd, 2026
"""
import pygame as py

"""
The CarlName class draws Carl's name to the screen 
"""
class CarlName(py.sprite.Sprite):
    """
    The initalize function for CarlName takes in x and y coordinate and uses them to draw the sprite at the correct position on the screen
    """
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((900,500),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Carl/without_backround/name_tag.png")
        self.img = py.transform.scale(self.img,(900,400))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y