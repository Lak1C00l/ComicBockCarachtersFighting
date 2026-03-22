"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task

Date Modified: Thursday, January 22nd, 2026
"""

import pygame as py
"""
The class KishaVPose draws Kisha's victory pose to the screen
"""
class KishaVpose(py.sprite.Sprite):
    """
    The initialize finction draws Kisha's victory pose to the screen using the x and y inputs to draw it to the correct part on the screen
    """
    def __init__(self,x,y,):
        super().__init__()
        self.image = py.Surface((700,800),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Kisha/without_backround/KishaVictoryPose.png")
        self.img = py.transform.scale(self.img,(700,800))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
