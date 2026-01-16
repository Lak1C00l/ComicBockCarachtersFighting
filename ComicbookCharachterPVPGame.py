import pygame as py
from SwitchingSprites4MrsCUNTiful import SwitchingMrsCUNTiful
from time import sleep



py.init()
size = 1500,750
screen = py.display.set_mode(size) 
py.display.set_caption("Lara's comicbook charachters fighting game")

carlSprites = py.sprite.Group()
kishaSprites = py.sprite.Group()
MrsCUNTifulSprites = py.sprite.Group()

carlFrozen = SwitchingMrsCUNTiful(400,400)
carlSprites.add(carlFrozen)

# # loading Mrs.CUNTiful's walk cycle
# CuntWalkFrame1 = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_1.png")
# CuntWalkFrame2 = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_2.png")
# CuntWalkFrame3 = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_3.png")
# CuntWalkFrame4 = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_4.png")

# def Jump(self,x,y,pixalMove):
#         self.rect.centerx = x
#         self.rect.centery = y

# def Duck(self,x,y):
#         self.rect.centerx = x
#         self.rect.centery = y
#         self.img = py.image.load("./CharSprites/MrsCUNTiful/duck")
#         self.img = py.transform.scale(self.img,(100,100))
#         self.image.blit(self.img,self.rect)


# def DashForward(self,x,y,pixalMove):
        
#         #change apperance of sprite
#         #self.image = py.Surface((100,100),py.SRCALPHA)
#         #get rect of sprite being used
#         #self.image = py.Surface((100,100),py.SRCALPHA)
#         #self.image.fill((0,0,0,0))
#         #self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_2.png")
#         #self.img = CuntWalkFrame2
#         #self.img = py.transform.scale(self.img,(100,100))
#         # self.rect = self.image.get_rect()
#         self.rect.centerx = x
#         self.rect.centery = y
#         self.image.blit(self.img,self.rect)
#         # while key is pressed keep dashing
#         self.rect.centerx += pixalMove

# def DashBack(self,x,y,pixalMove):
#         self.rect.centerx = x
#         self.rect.centery = y
#         #change apperance of sprite
#         #self.image = py.Surface((100,100),py.SRCALPHA)
#         #self.rect = self.image.get_rect()
#         #self.img = py.image.load("./CharSprites/MrsCUNTiful/walk_cycle/walk_cycle_frame_3.png")
#         #self.img = py.transform.scale(self.img,(100,100))
#         #self.image.blit(self.img,self.rect)

#         # while key is pressed keep dashing
#         self.rect.centerx -= pixalMove
# def Walkcycle(self,x,y,playerIdle):
#         self.rect.centerx = x
#         self.rect.centery = y


playing = True

while playing:
    screen.fill((0,0,0))
    py.event.pump()

    keys = py.key.get_pressed()
    carlSprites.draw(screen)
    if keys[py.K_w]:
        print("cool")
        tempX = int(carlFrozen.rect.centerx)
        tempY = int(carlFrozen.rect.centery)
        carlFrozen.Jump(tempX,tempY,5)
                # change from any sprite to jump
        carlSprites.draw(screen)
    if keys[py.K_a]:
        print("Jump")
        tempX = int(carlFrozen.rect.centerx)
        tempY = int(carlFrozen.rect.centery)
        
        carlFrozen.DashBack(tempX,tempY,5)
                # change from any sprite to dask back
        carlSprites.draw(screen)


    if keys[py.K_s]:
        print("cool")
                # change from any sprite to duck
    if keys[py.K_d]:
        print("cool")
        tempX = int(carlFrozen.rect.centerx)
        tempY = int(carlFrozen.rect.centery)
        carlFrozen.DashForward(tempX,tempY,5)

            # change from any sprite to dash forward
    carlSprites.draw(screen)
    carlSprites.update()
    py.display.update()
    sleep(10/1000)

    