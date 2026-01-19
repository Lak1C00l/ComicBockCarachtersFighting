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

MrsCUNTIfulBase = SwitchingMrsCUNTiful(400,400)
carlSprites.add(MrsCUNTIfulBase)

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
        tempX = int(MrsCUNTIfulBase.rect.centerx)
        tempY = int(MrsCUNTIfulBase.rect.centery)
        MrsCUNTIfulBase.Jump(5)
                # change from any sprite to jump
        carlSprites.draw(screen)


    if keys[py.K_a]:
        print("cool")
        MrsCUNTIfulBase.DashBackCUNT(5)
        MrsCUNTifulSprites.draw(screen)


    if keys[py.K_s]:
        tempX = int(MrsCUNTIfulBase.rect.centerx)
        tempY = int(MrsCUNTIfulBase.rect.centery)
        # change from any sprite to duck
        MrsCUNTIfulBase.Duck(tempX,tempY)

    if keys[py.K_d]:
        print("cool")
        MrsCUNTIfulBase.DashForwardCUNT(5)

            # change from any sprite to dash forward
    carlSprites.draw(screen)
    MrsCUNTifulSprites.draw(screen)
    carlSprites.update()
    MrsCUNTifulSprites.update()
    py.display.update()
    sleep(10/1000)

    