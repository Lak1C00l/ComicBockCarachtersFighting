import pygame as py
from SwitchingSprites4MrsCUNTifulP1 import SwitchingMrsCUNTiful
from SwitchingSprites4CarlP1 import SwitchingCarl
from SwitchingSprites4KishaP1 import SwitchingKisha
from time import sleep

timeWhenNoButtonPressed = 100
DuckHappened1 = False
JumpHappened1 = False
DuckHappened2 = False
JumpHappened2 = False
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
MrsCUNTifulSprites = py.sprite.Group()

if charSelected4Player1 == 1:
    player2 = False
    MrsCUNTIfulBase = SwitchingMrsCUNTiful(400,400,player2)
    MrsCUNTifulSprites.add(MrsCUNTIfulBase)
elif charSelected4Player2 == 1:
    MrsCUNTIfulBase = SwitchingMrsCUNTiful(1200,400,player2)
    MrsCUNTifulSprites.add(MrsCUNTIfulBase)
if charSelected4Player1 == 2:
    player2 = False
    CarlBase = SwitchingCarl(400,400,player2)
    carlSprites.add(CarlBase)
elif charSelected4Player2 == 2:
    CarlBase = SwitchingCarl(1200,400,player2)
    carlSprites.add(CarlBase)
if charSelected4Player1 == 3:
    player2 = False
    KishaBase = SwitchingKisha(400,375,player2)
    kishaSprites.add(KishaBase)
elif charSelected4Player2 == 3:
    KishaBase = SwitchingKisha(1200,375,player2)
    kishaSprites.add(KishaBase)


playing = True

while playing:
    screen.fill((0,0,0))
    py.event.pump()

    keys = py.key.get_pressed()
    MrsCUNTifulSprites.draw(screen)

    match charSelected4Player1:
        case 1:
            player2 = False
            # if not keys[py.K_a] or not keys[py.K_d] or not keys[py.K_e] or not keys[py.K_q] or not keys[py.K_s] or not keys[py.K_w]:
            #     MrsCUNTIfulBase.IdleCUNT(DuckHappened1,JumpHappened2)
            #     DuckHappened1 = False
            #     JumpHappened2 = False
                
            if keys[py.K_w]:
                 
                tempY = int(MrsCUNTIfulBase.rect.bottom)  
                if not JumpHappened1:
                    MrsCUNTIfulBase.jumpy = tempY
                    MrsCUNTIfulBase.is_jump = True

                if DuckHappened1:
                    MrsCUNTIfulBase.jumpy = 575

                if MrsCUNTIfulBase.rect.bottom>=MrsCUNTIfulBase.jumpy-100 and MrsCUNTIfulBase.is_jump:
                    MrsCUNTIfulBase.Jump(7,DuckHappened1,player2)

                if MrsCUNTIfulBase.rect.bottom<=MrsCUNTIfulBase.jumpy-100 or (not MrsCUNTIfulBase.is_jump and MrsCUNTIfulBase.rect.bottom<=MrsCUNTIfulBase.jumpy and not DuckHappened1):
                    MrsCUNTIfulBase.is_jump = False
                    MrsCUNTIfulBase.Jump(5,DuckHappened1,player2)

                if MrsCUNTIfulBase.rect.bottom>=MrsCUNTIfulBase.jumpy and MrsCUNTIfulBase.is_jump==False:
                    MrsCUNTIfulBase.is_jump = True
                
                JumpHappened1 = True
                DuckHappened1 = False


            if keys[py.K_a]:
                print("cool")
                MrsCUNTIfulBase.DashBackCUNT(-7,DuckHappened1,JumpHappened1,player2)
                MrsCUNTifulSprites.draw(screen)
                DuckHappened1 = False
                JumpHappened1 = False


            if keys[py.K_s]:
                tempX = int(MrsCUNTIfulBase.rect.centerx)
                tempY = int(MrsCUNTIfulBase.rect.centery)
                # change from any sprite to duck
                MrsCUNTIfulBase.Duck(tempX,tempY,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = True
                JumpHappened1 = False


            if keys[py.K_d]:
                print("cool")
                MrsCUNTIfulBase.DashForwardCUNT(-7,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False
                    # change from any sprite to dash forward

            if keys[py.K_q]:
                MrsCUNTIfulBase.Block(DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False

            if keys[py.K_e]:
                MrsCUNTIfulBase.IdleCUNT(DuckHappened1,JumpHappened1,player2)
                MrsCUNTIfulBase.Attack(DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False

            

            #when player has not clicked button 
            # for event in py.event.get():
            #     if event.type == py.KEYUP:
            #         if timeWhenNoButtonPressed <= 100:
            #             timeWhenNoButtonPressed += 1
            #         if timeWhenNoButtonPressed == 100:
            #             MrsCUNTIfulBase.Walkcycle(DuckHappened1,JumpHappened2)
            #             DuckHappened1 = False
            #             JumpHappened2 = False

        case 2:
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


            if keys[py.K_a]:
                print("cool")
                CarlBase.DashBackCarl(15,DuckHappened1,JumpHappened1,player2)
                carlSprites.draw(screen)
                DuckHappened1 = False
                JumpHappened1 = False


            if keys[py.K_s]:
                tempX = int(CarlBase.rect.centerx)
                tempY = int(CarlBase.rect.centery)
                # change from any sprite to duck
                CarlBase.Duck(tempX,tempY,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = True
                JumpHappened1 = False


            if keys[py.K_d]:
                CarlBase.DashForwardCarl(15,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False
                    # change from any sprite to dash forward

            if keys[py.K_q]:
                CarlBase.Block(DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        CarlBase.Walkcycle(DuckHappened1,JumpHappened1,player2)
                        DuckHappened1 = False
                        JumpHappened1 = False
        
        case 3:
            player2 = False
            if keys[py.K_w]:
                tempY = int(KishaBase.rect.bottom)  
                if not JumpHappened1:
                    KishaBase.jumpy = tempY
                    KishaBase.is_jump = True

                if DuckHappened1:
                    KishaBase.jumpy = 575

                if KishaBase.rect.bottom>=KishaBase.jumpy-100 and KishaBase.is_jump:
                    KishaBase.Jump(7,DuckHappened1,player2)

                if KishaBase.rect.bottom<=KishaBase.jumpy-100 or (not KishaBase.is_jump and KishaBase.rect.bottom<=KishaBase.jumpy and not DuckHappened1):
                    KishaBase.is_jump = False
                    KishaBase.Jump(5,DuckHappened1,player2)

                if KishaBase.rect.bottom>=KishaBase.jumpy and KishaBase.is_jump==False:
                    KishaBase.is_jump = True
                
                JumpHappened1 = True
                DuckHappened1 = False


            if keys[py.K_a]:
                KishaBase.DashBackKisha(7,DuckHappened1,JumpHappened1,player2)
                kishaSprites.draw(screen)
                DuckHappened1 = False
                JumpHappened1 = False


            if keys[py.K_s]:
                tempX = int(KishaBase.rect.centerx)
                tempY = int(KishaBase.rect.centery)
                # change from any sprite to duck
                KishaBase.Duck(tempX,tempY,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = True
                JumpHappened1 = False


            if keys[py.K_d]:
                KishaBase.DashForwardKisha(7,DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False
                    # change from any sprite to dash forward

            if keys[py.K_q]:
                KishaBase.Block(DuckHappened1,JumpHappened1,player2)
                DuckHappened1 = False
                JumpHappened1 = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        KishaBase.Walkcycle(DuckHappened1,JumpHappened1,player2)
                        DuckHappened1 = False
                        JumpHappened1 = False
                    

    match charSelected4Player2:
        case 1:
            player2 = True
            # if not keys[py.K_a] or not keys[py.K_d] or not keys[py.K_e] or not keys[py.K_q] or not keys[py.K_s] or not keys[py.K_w]:
            #     MrsCUNTIfulBase.IdleCUNT(DuckHappened1,JumpHappened2)
            #     DuckHappened1 = False
            #     JumpHappened2 = False
                
            if keys[py.K_UP]:
                 
                tempY = int(MrsCUNTIfulBase.rect.bottom)  
                if not JumpHappened2:
                    MrsCUNTIfulBase.jumpy = tempY
                    MrsCUNTIfulBase.is_jump = True

                if DuckHappened2:
                    MrsCUNTIfulBase.jumpy = 575

                if MrsCUNTIfulBase.rect.bottom>=MrsCUNTIfulBase.jumpy-100 and MrsCUNTIfulBase.is_jump:
                    MrsCUNTIfulBase.Jump(7,DuckHappened2,player2)

                if MrsCUNTIfulBase.rect.bottom<=MrsCUNTIfulBase.jumpy-100 or (not MrsCUNTIfulBase.is_jump and MrsCUNTIfulBase.rect.bottom<=MrsCUNTIfulBase.jumpy and not DuckHappened2):
                    MrsCUNTIfulBase.is_jump = False
                    MrsCUNTIfulBase.Jump(5,DuckHappened2,player2)

                if MrsCUNTIfulBase.rect.bottom>=MrsCUNTIfulBase.jumpy and MrsCUNTIfulBase.is_jump==False:
                    MrsCUNTIfulBase.is_jump = True
                
                JumpHappened2 = True
                DuckHappened2 = False


            if keys[py.K_RIGHT]:
                MrsCUNTIfulBase.DashBackCUNT(-7,DuckHappened2,JumpHappened2,player2)
                MrsCUNTifulSprites.draw(screen)
                DuckHappened2 = False
                JumpHappened2 = False


            if keys[py.K_DOWN]:
                tempX = int(MrsCUNTIfulBase.rect.centerx)
                tempY = int(MrsCUNTIfulBase.rect.centery)
                # change from any sprite to duck
                MrsCUNTIfulBase.Duck(tempX,tempY,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = True
                JumpHappened2 = False


            if keys[py.K_LEFT]:
                print("cool")
                MrsCUNTIfulBase.DashForwardCUNT(-7,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                    # change from any sprite to dash forward

            if keys[py.K_8]:
                MrsCUNTIfulBase.Block(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            if keys[py.K_9]:
                MrsCUNTIfulBase.IdleCUNT(DuckHappened2,JumpHappened2,player2)
                MrsCUNTIfulBase.Attack(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            

            #when player has not clicked button 
            # for event in py.event.get():
            #     if event.type == py.KEYUP:
            #         if timeWhenNoButtonPressed <= 100:
            #             timeWhenNoButtonPressed += 1
            #         if timeWhenNoButtonPressed == 100:
            #             MrsCUNTIfulBase.Walkcycle(DuckHappened1,JumpHappened2)
            #             DuckHappened1 = False
            #             JumpHappened2 = False

        case 2:
            player2 = True

            if keys[py.K_UP]:
                 
                tempY = int(CarlBase.rect.bottom)  
                if not JumpHappened2:
                    CarlBase.jumpy = tempY
                    CarlBase.is_jump = True

                if DuckHappened2:
                    CarlBase.jumpy = 575

                if CarlBase.rect.bottom>=CarlBase.jumpy-100 and CarlBase.is_jump:
                    CarlBase.Jump(7,DuckHappened2,player2)

                if CarlBase.rect.bottom<=CarlBase.jumpy-100 or (not CarlBase.is_jump and CarlBase.rect.bottom<=CarlBase.jumpy and not DuckHappened2):
                    CarlBase.is_jump = False
                    CarlBase.Jump(5,DuckHappened2,player2)

                if CarlBase.rect.bottom>=CarlBase.jumpy and CarlBase.is_jump==False:
                    CarlBase.is_jump = True
                
                JumpHappened2 = True
                DuckHappened2 = False


            if keys[py.K_RIGHT]:
                print("cool")
                CarlBase.DashBackCarl(15,DuckHappened2,JumpHappened2,player2)
                carlSprites.draw(screen)
                DuckHappened2 = False
                JumpHappened2 = False


            if keys[py.K_DOWN]:
                tempX = int(CarlBase.rect.centerx)
                tempY = int(CarlBase.rect.centery)
                # change from any sprite to duck
                CarlBase.Duck(tempX,tempY,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = True
                JumpHappened2 = False


            if keys[py.K_LEFT]:
                CarlBase.DashForwardCarl(15,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                    # change from any sprite to dash forward

            if keys[py.K_8]:
                CarlBase.Block(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        CarlBase.Walkcycle(DuckHappened2,JumpHappened2,player2)
                        DuckHappened2 = False
                        JumpHappened2 = False
        
        case 3:
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


            if keys[py.K_RIGHT]:
                KishaBase.DashBackKisha(9,DuckHappened2,JumpHappened2,player2)
                kishaSprites.draw(screen)
                DuckHappened2 = False
                JumpHappened2 = False


            if keys[py.K_DOWN]:
                tempX = int(KishaBase.rect.centerx)
                tempY = int(KishaBase.rect.centery)
                # change from any sprite to duck
                KishaBase.Duck(tempX,tempY,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = True
                JumpHappened2 = False


            if keys[py.K_LEFT]:
                KishaBase.DashForwardKisha(9,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                    # change from any sprite to dash forward

            if keys[py.K_8]:
                KishaBase.Block(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        KishaBase.Walkcycle(DuckHappened2,JumpHappened2,player2)
                        DuckHappened2 = False
                        JumpHappened2 = False
            
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

    