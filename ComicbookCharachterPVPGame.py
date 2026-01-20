import pygame as py
from SwitchingSprites4MrsCUNTifulP1 import SwitchingMrsCUNTiful
from SwitchingSprites4CarlP1 import SwitchingCarl
from SwitchingSprites4KishaP1 import SwitchingKisha
from time import sleep

timeWhenNoButtonPressed = 100
DuckHappened = False
JumpHappened = False
ButtonPressed = True
step = 0

py.init()
size = 1500,750
screen = py.display.set_mode(size) 
py.display.set_caption("Lara's comicbook charachters fighting game")

charSelected4Player1 = 3
charSelected4Player2 = 1


carlSprites = py.sprite.Group()
kishaSprites = py.sprite.Group()
MrsCUNTifulSprites = py.sprite.Group()

if charSelected4Player1 == 1:
    MrsCUNTIfulBase = SwitchingMrsCUNTiful(400,400)
    MrsCUNTifulSprites.add(MrsCUNTIfulBase)

elif charSelected4Player1 == 2:
    CarlBase = SwitchingCarl(400,450)
    carlSprites.add(CarlBase)

elif charSelected4Player1 == 3:
    KishaBase = SwitchingKisha(400,375)
    kishaSprites.add(KishaBase)


playing = True

while playing:
    screen.fill((0,0,0))
    py.event.pump()

    keys = py.key.get_pressed()
    MrsCUNTifulSprites.draw(screen)

    match charSelected4Player1:
        case 1:
            if keys[py.K_w]:
                 
                tempY = int(MrsCUNTIfulBase.rect.bottom)  
                if not JumpHappened:
                    MrsCUNTIfulBase.jumpy = tempY
                    MrsCUNTIfulBase.is_jump = True

                if DuckHappened:
                    MrsCUNTIfulBase.jumpy = 575

                if MrsCUNTIfulBase.rect.bottom>=MrsCUNTIfulBase.jumpy-100 and MrsCUNTIfulBase.is_jump:
                    MrsCUNTIfulBase.Jump(7,DuckHappened)

                if MrsCUNTIfulBase.rect.bottom<=MrsCUNTIfulBase.jumpy-100 or (not MrsCUNTIfulBase.is_jump and MrsCUNTIfulBase.rect.bottom<=MrsCUNTIfulBase.jumpy and not DuckHappened):
                    MrsCUNTIfulBase.is_jump = False
                    MrsCUNTIfulBase.Jump(5,DuckHappened)

                if MrsCUNTIfulBase.rect.bottom>=MrsCUNTIfulBase.jumpy and MrsCUNTIfulBase.is_jump==False:
                    MrsCUNTIfulBase.is_jump = True
                
                JumpHappened = True
                DuckHappened = False


            if keys[py.K_a]:
                print("cool")
                MrsCUNTIfulBase.DashBackCUNT(7,DuckHappened,JumpHappened)
                MrsCUNTifulSprites.draw(screen)
                DuckHappened = False
                JumpHappened = False


            if keys[py.K_s]:
                tempX = int(MrsCUNTIfulBase.rect.centerx)
                tempY = int(MrsCUNTIfulBase.rect.centery)
                # change from any sprite to duck
                MrsCUNTIfulBase.Duck(tempX,tempY,DuckHappened,JumpHappened)
                DuckHappened = True
                JumpHappened = False


            if keys[py.K_d]:
                print("cool")
                MrsCUNTIfulBase.DashForwardCUNT(7,DuckHappened,JumpHappened)
                DuckHappened = False
                JumpHappened = False
                    # change from any sprite to dash forward

            if keys[py.K_q]:
                MrsCUNTIfulBase.Block(DuckHappened,JumpHappened)
                DuckHappened = False
                JumpHappened = False

            if keys[py.K_e]:
                MrsCUNTIfulBase.Attack(DuckHappened,JumpHappened)
                DuckHappened = False
                JumpHappened = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        MrsCUNTIfulBase.Walkcycle(DuckHappened,JumpHappened)
                        DuckHappened = False
                        JumpHappened = False

        case 2:
            if keys[py.K_w]:
                 
                tempY = int(CarlBase.rect.bottom)  
                if not JumpHappened:
                    CarlBase.jumpy = tempY
                    CarlBase.is_jump = True

                if DuckHappened:
                    CarlBase.jumpy = 575

                if CarlBase.rect.bottom>=CarlBase.jumpy-100 and CarlBase.is_jump:
                    CarlBase.Jump(7,DuckHappened)

                if CarlBase.rect.bottom<=CarlBase.jumpy-100 or (not CarlBase.is_jump and CarlBase.rect.bottom<=CarlBase.jumpy and not DuckHappened):
                    CarlBase.is_jump = False
                    CarlBase.Jump(5,DuckHappened)

                if CarlBase.rect.bottom>=CarlBase.jumpy and CarlBase.is_jump==False:
                    CarlBase.is_jump = True
                
                JumpHappened = True
                DuckHappened = False


            if keys[py.K_a]:
                print("cool")
                CarlBase.DashBackCarl(15,DuckHappened,JumpHappened)
                carlSprites.draw(screen)
                DuckHappened = False
                JumpHappened = False


            if keys[py.K_s]:
                tempX = int(CarlBase.rect.centerx)
                tempY = int(CarlBase.rect.centery)
                # change from any sprite to duck
                CarlBase.Duck(tempX,tempY,DuckHappened,JumpHappened)
                DuckHappened = True
                JumpHappened = False


            if keys[py.K_d]:
                CarlBase.DashForwardCarl(15,DuckHappened,JumpHappened)
                DuckHappened = False
                JumpHappened = False
                    # change from any sprite to dash forward

            if keys[py.K_q]:
                CarlBase.Block(DuckHappened,JumpHappened)
                DuckHappened = False
                JumpHappened = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        CarlBase.Walkcycle(DuckHappened,JumpHappened)
                        DuckHappened = False
                        JumpHappened = False
        
        case 3:
            if keys[py.K_w]:
                tempY = int(KishaBase.rect.bottom)  
                if not JumpHappened:
                    KishaBase.jumpy = tempY
                    KishaBase.is_jump = True

                if DuckHappened:
                    KishaBase.jumpy = 575

                if KishaBase.rect.bottom>=KishaBase.jumpy-100 and KishaBase.is_jump:
                    KishaBase.Jump(7,DuckHappened)

                if KishaBase.rect.bottom<=KishaBase.jumpy-100 or (not KishaBase.is_jump and KishaBase.rect.bottom<=KishaBase.jumpy and not DuckHappened):
                    KishaBase.is_jump = False
                    KishaBase.Jump(5,DuckHappened)

                if KishaBase.rect.bottom>=KishaBase.jumpy and KishaBase.is_jump==False:
                    KishaBase.is_jump = True
                
                JumpHappened = True
                DuckHappened = False


            if keys[py.K_a]:
                KishaBase.DashBackKisha(9,DuckHappened,JumpHappened)
                kishaSprites.draw(screen)
                DuckHappened = False
                JumpHappened = False


            if keys[py.K_s]:
                tempX = int(KishaBase.rect.centerx)
                tempY = int(KishaBase.rect.centery)
                # change from any sprite to duck
                KishaBase.Duck(tempX,tempY,DuckHappened,JumpHappened)
                DuckHappened = True
                JumpHappened = False


            if keys[py.K_d]:
                KishaBase.DashForwardKisha(9,DuckHappened,JumpHappened)
                DuckHappened = False
                JumpHappened = False
                    # change from any sprite to dash forward

            if keys[py.K_q]:
                KishaBase.Block(DuckHappened,JumpHappened)
                DuckHappened = False
                JumpHappened = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        KishaBase.Walkcycle(DuckHappened,JumpHappened)
                        DuckHappened = False
                        JumpHappened = False
                    
            
    # start time
    # if time is larger than 200 then start walk cycle

    carlSprites.draw(screen)
    MrsCUNTifulSprites.draw(screen)
    kishaSprites.draw(screen)
    carlSprites.update()
    MrsCUNTifulSprites.update()
    kishaSprites.update()
    py.display.update()
    sleep(10/1000)

    