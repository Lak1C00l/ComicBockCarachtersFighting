import pygame as py

class KishaVpose(py.sprite.Sprite):
    def __init__(self,x,y,):
        super().__init__()
        self.image = py.Surface((500,500),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.img = py.image.load("./CharSprites/Kisha/without_backround/nameTag.png")
        self.img = py.transform.scale(self.img,(500,500))
        self.image.blit(self.img,self.rect)
        self.rect.centerx = x
        self.rect.centery = y
