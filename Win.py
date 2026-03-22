"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task

Date Modified: Thursday, January 22nd, 2026
"""

import pygame as py

class WinLogo(py.sprite.Sprite):
    """
    The initialize function draws the win sprite at the spot where the inputs of x and y indicate it to
    """
    def __init__(self,x,y,):
        super().__init__()
        self.image = py.Surface((500,500),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/winLogo.png")
        self.img = py.transform.scale(self.img,(500,500))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
