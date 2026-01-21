import pygame as py

class StartGameButton(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((100,100),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        py.draw.rect(self.image,(0,255,0),py.Rect(50,50,50,50))