import pygame as py

class P1HealthBar(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((500,50),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        py.draw.rect(self.image,(0,255,0),py.Rect(10,10,500,50))

    def damageTakenP1(self,totalDamage, hitDamage): 
        

        print(f"hitDamage: {hitDamage}, totalDamage: {totalDamage}")

        totalDamage += hitDamage
        
        print(f"hitDamage: {hitDamage}, totalDamage: {totalDamage}")

        newWidth = 500 - totalDamage
        print(f"newWidth : {newWidth}")

        # print(f"self.image.get_width(): {self.image.get_width()}")
        # print(f"self.rect.width: {self.rect.width}")

        self.image.fill((0,0,0,0))
        py.draw.rect(self.image,(0,255,0),py.Rect(10,10,newWidth,50))

        return totalDamage


        





        # self.image = py.Surface((500,50),py.SRCALPHA)

        # # print(self.image.get_width())
        # # print(self.image.get_height())
        
        # print(f"before {self.rect.width}")
        


        # self.rect = self.image.get_rect()
        # self.rect.centerx = x
        # self.rect.centery = y
        # self.rect.width =  250

        # print(self.rect.width)