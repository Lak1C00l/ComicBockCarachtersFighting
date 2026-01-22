import pygame as py
from SwitchingSprites4CarlP1 import SwitchingCarl
from SwitchingSprites4KishaP1 import SwitchingKisha
from HealthBarP1 import P1HealthBar
from HealthBarP2 import P2HealthBar
from KishaVictory import KishaVpose
from KishaNameTag import KishaName
from time import sleep

timeWhenNoButtonPressed = 100
DuckHappened1 = False
JumpHappened1 = False
DuckHappened2 = False
JumpHappened2 = False
P1IsHitting = False
P2IsHitting = False
P1IsBlocking = False
P2IsBlocking = False
ButtonPressed = True
player2 = True


py.init()
size = 1500,750
screen = py.display.set_mode(size) 
py.display.set_caption("Lara's comicbook charachters fighting game")

charSelected4Player1 = 1
charSelected4Player2 = 2


carlSprites = py.sprite.Group()
kishaSprites = py.sprite.Group()
healthBars = py.sprite.Group()
victory = py.sprite.Group()
healthBar1 = P1HealthBar(300,100)
healthBar2 = P2HealthBar(1190,100)
healthBars.add(healthBar1)
healthBars.add(healthBar2)
noHealthBar1 = 0
P1DamageAll = 0

P2DamageAll = 0



    

if charSelected4Player1 == 1:
    player2 = False
    CarlBase = SwitchingCarl(400,400,player2)
    carlSprites.add(CarlBase)
if charSelected4Player2 == 2:
    player2 = True
    KishaBase = SwitchingKisha(1200,375,player2)
    kishaSprites.add(KishaBase)


playing = True

while playing:
    screen.fill((0,0,0))
    py.event.pump()

    keys = py.key.get_pressed()

    if charSelected4Player1 == 1:
            player2 = False
            if keys[py.K_w]:
                 
                tempY = int(CarlBase.rect.bottom)  
                if not JumpHappened1:
                    CarlBase.jumpy = tempY
                    CarlBase.is_jump = True

                if DuckHappened1:
                    CarlBase.jumpy = 575

                if CarlBase.rect.bottom>=CarlBase.jumpy-100 and CarlBase.is_jump:
                    CarlBase.Jump(7,DuckHappened1,player2)

                if CarlBase.rect.bottom<=CarlBase.jumpy-100 or (not CarlBase.is_jump and CarlBase.rect.bottom<=CarlBase.jumpy and not DuckHappened1):
                    CarlBase.is_jump = False
                    CarlBase.Jump(5,DuckHappened1,player2)

                if CarlBase.rect.bottom>=CarlBase.jumpy and CarlBase.is_jump==False:
                    CarlBase.is_jump = True
                
                JumpHappened1 = True
                DuckHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False


            if keys[py.K_a]:
                print("cool")
                CarlBase.DashBackCarl(15,DuckHappened1,JumpHappened1,player2)
                carlSprites.draw(screen)
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False


            if keys[py.K_s]:
                tempX = int(CarlBase.rect.centerx)
                tempY = int(CarlBase.rect.centery)
                # change from any sprite to duck
                CarlBase.Duck(tempX,tempY,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = True
                JumpHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False

            # change from any sprite to dash forward
            if keys[py.K_d]:
                CarlBase.DashForwardCarl(15,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False
                    
            if keys[py.K_q]:
                CarlBase.Block(DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsHitting = False
                P1IsBlocking = True

            if keys[py.K_e]:
                CarlBase.Attack(DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsBlocking = False
                P1IsHitting = True

            if P2IsHitting and KishaBase.rect.colliderect(CarlBase) and P1IsBlocking == False:
                CarlBase.Hit(DuckHappened1,JumpHappened1,player2)
                P1DamageAll = healthBar1.damageTakenP1(P1DamageAll,5)
                
                DuckHappened1 = False
                JumpHappened1 = False
                DuckHappened2 = False
                JumpHappened2 = False

            if P1DamageAll >= 500:
                victoryPose = KishaVpose(500,500)
                nameTag = KishaName(1200,500)
                victory.add(nameTag)
                victory.add(victoryPose)
                
                
        

    if charSelected4Player2 == 2:
            player2 = True
            if keys[py.K_UP]:
                tempY = int(KishaBase.rect.bottom)  
                if not JumpHappened2:
                    KishaBase.jumpy = tempY
                    KishaBase.is_jump = True

                if DuckHappened2:
                    KishaBase.jumpy = 575

                if KishaBase.rect.bottom>=KishaBase.jumpy-100 and KishaBase.is_jump:
                    KishaBase.Jump(7,DuckHappened2,player2)

                if KishaBase.rect.bottom<=KishaBase.jumpy-100 or (not KishaBase.is_jump and KishaBase.rect.bottom<=KishaBase.jumpy and not DuckHappened2):
                    KishaBase.is_jump = False
                    KishaBase.Jump(5,DuckHappened2,player2)

                if KishaBase.rect.bottom>=KishaBase.jumpy and KishaBase.is_jump==False:
                    KishaBase.is_jump = True
                
                JumpHappened2 = True
                DuckHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False


            if keys[py.K_RIGHT]:
                KishaBase.DashBackKisha(9,DuckHappened2,JumpHappened2,player2)
                kishaSprites.draw(screen)
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False


            if keys[py.K_DOWN]:
                tempX = int(KishaBase.rect.centerx)
                tempY = int(KishaBase.rect.centery)
                # change from any sprite to duck
                KishaBase.Duck(tempX,tempY,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = True
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False


            if keys[py.K_LEFT]:
                KishaBase.DashForwardKisha(9,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False
                    # change from any sprite to dash forward

            if keys[py.K_0]:
                KishaBase.Block(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = True
                P2IsHitting = False

            if keys[py.K_8]:
                KishaBase.Attack(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = True


            
            if P1IsHitting and CarlBase.rect.colliderect(KishaBase) and P2IsBlocking == False:
                KishaBase.Hit(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            
    # start time
    # if time is larger than 200 then start walk cycle

    carlSprites.draw(screen)
    kishaSprites.draw(screen)
    healthBars.draw(screen)
    victory.draw(screen)
    carlSprites.update()
    kishaSprites.update()
    healthBars.update()
    victory.update()
    py.display.update()
    sleep(10/1000)