import pygame as py
from SwitchingSprites4MrsCUNTifulP1 import SwitchingMrsCUNTiful
from SwitchingSprites4CarlP1 import SwitchingCarl
from SwitchingSprites4KishaP1 import SwitchingKisha
from SelectCharachterButtonP1 import SelectCharButton1
from SelectCharachterButtonP2 import SelectCharButton2
from time import sleep

kishaHealth = 1000
carlHealth = 1000
MrsCUNTifulHealth = 1000
closeAttack = 150
farAttack = 50

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

charSelected4Player1 = 2
charSelected4Player2 = 3


carlSprites = py.sprite.Group()
KishaSprites = py.sprite.Group()
MrsCUNTifulSprites = py.sprite.Group()
carlSprites2 = py.sprite.Group()
KishaSprites2 = py.sprite.Group()
MrsCUNTifulSprites2 = py.sprite.Group()

selectButtonP1 = py.sprite.Group()
selectButtonP2 = py.sprite.Group()


selectButton1 = SelectCharButton1(175,600)
selectButtonP1.add(selectButton1)
selectButton2 = SelectCharButton2(1275,600)
selectButtonP2.add(selectButton2)


if charSelected4Player1 == 1:
    player2 = False
    MrsCUNTIfulBase = SwitchingMrsCUNTiful(400,400,player2)
    MrsCUNTifulSprites.add(MrsCUNTIfulBase)
elif charSelected4Player2 == 1:
    player2 = True
    MrsCUNTIfulBase2 = SwitchingMrsCUNTiful(1200,400,player2)
    MrsCUNTifulSprites2.add(MrsCUNTIfulBase2)
if charSelected4Player1 == 2:
    player2 = False
    CarlBase = SwitchingCarl(400,400,player2)
    carlSprites.add(CarlBase)
elif charSelected4Player2 == 2:
    player2 = True
    CarlBase2 = SwitchingCarl(1200,400,player2)
    carlSprites2.add(CarlBase2)
if charSelected4Player1 == 3:
    player2 = False
    KishaBase = SwitchingKisha(400,375,player2)
    KishaSprites.add(KishaBase)
elif charSelected4Player2 == 3:
    player2 = True
    KishaBase2 = SwitchingKisha(1200,375,player2)
    KishaSprites2.add(KishaBase2)




playing = True

while playing:
    screen.fill((0,0,0))
    py.event.pump()

    keys = py.key.get_pressed()
    MrsCUNTifulSprites.draw(screen)
    prev_select1 = charSelected4Player1
    prev_slect2 = charSelected4Player2
    for event in py.event.get():
        if event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            print(pos)
            if selectButton1.rect.collidepoint(pos):
                if charSelected4Player1 < 4:
                    charSelected4Player1 +=1
                elif charSelected4Player1 >= 3:
                    charSelected4Player1 = 1
            if selectButton2.rect.collidepoint(pos):
                if charSelected4Player2 < 4:
                    charSelected4Player2 +=1
                elif charSelected4Player2 >= 3:
                    charSelected4Player2 = 1


    match charSelected4Player1:
        case 1:
            player2 = False
            MrsCUNTifulSprites.empty()
            carlSprites.empty()
            KishaSprites.empty()
            MrsCUNTIfulBase = SwitchingMrsCUNTiful(400,400,player2)
            MrsCUNTifulSprites.add(MrsCUNTIfulBase)
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


        case 2:
            player2 = False
            carlSprites.empty()
            MrsCUNTifulSprites.empty()
            KishaSprites.empty()
            CarlBase = SwitchingCarl(400,400,player2)
            carlSprites.add(CarlBase)
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
            carlSprites.empty()
            MrsCUNTifulSprites.empty()
            KishaSprites.empty()
            KishaBase = SwitchingKisha(400,400,player2)
            KishaSprites.add(KishaBase)
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
                KishaSprites.draw(screen)
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

                    

    match charSelected4Player2:
        case 1:
            player2 = True
            MrsCUNTifulSprites2.empty()
            carlSprites2.empty()
            KishaSprites2.empty()
            MrsCUNTIfulBase2 = SwitchingMrsCUNTiful(1200,400,player2)
            MrsCUNTifulSprites2.add(MrsCUNTIfulBase2)
            
                
            if keys[py.K_UP]:
                 
                tempY = int(MrsCUNTIfulBase2.rect.bottom)  
                if not JumpHappened2:
                    MrsCUNTIfulBase2.jumpy = tempY
                    MrsCUNTIfulBase2.is_jump = True

                if DuckHappened2:
                    MrsCUNTIfulBase2.jumpy = 575

                if MrsCUNTIfulBase2.rect.bottom>=MrsCUNTIfulBase2.jumpy-100 and MrsCUNTIfulBase2.is_jump:
                    MrsCUNTIfulBase2.Jump(7,DuckHappened2,player2)

                if MrsCUNTIfulBase2.rect.bottom<=MrsCUNTIfulBase2.jumpy-100 or (not MrsCUNTIfulBase2.is_jump and MrsCUNTIfulBase2.rect.bottom<=MrsCUNTIfulBase2.jumpy and not DuckHappened2):
                    MrsCUNTIfulBase2.is_jump = False
                    MrsCUNTIfulBase2.Jump(5,DuckHappened2,player2)

                if MrsCUNTIfulBase2.rect.bottom>=MrsCUNTIfulBase2.jumpy and MrsCUNTIfulBase2.is_jump==False:
                    MrsCUNTIfulBase2.is_jump = True
                
                JumpHappened2 = True
                DuckHappened2 = False


            if keys[py.K_RIGHT]:
                MrsCUNTIfulBase2.DashBackCUNT(-7,DuckHappened2,JumpHappened2,player2)
                MrsCUNTifulSprites.draw(screen)
                DuckHappened2 = False
                JumpHappened2 = False


            if keys[py.K_DOWN]:
                tempX = int(MrsCUNTIfulBase2.rect.centerx)
                tempY = int(MrsCUNTIfulBase2.rect.centery)
                # change from any sprite to duck
                MrsCUNTIfulBase2.Duck(tempX,tempY,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = True
                JumpHappened2 = False


            if keys[py.K_LEFT]:
                print("cool")
                MrsCUNTIfulBase2.DashForwardCUNT(-7,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                    # change from any sprite to dash forward

            if keys[py.K_8]:
                MrsCUNTIfulBase2.Block(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            if keys[py.K_9]:
                MrsCUNTIfulBase2.IdleCUNT(DuckHappened2,JumpHappened2,player2)
                MrsCUNTIfulBase2.Attack(DuckHappened2,JumpHappened2,player2)
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
            MrsCUNTifulSprites2.empty()
            carlSprites2.empty()
            KishaSprites2.empty()
            CarlBase2 = SwitchingCarl(1200,400,player2)
            carlSprites.add(CarlBase2)

            if keys[py.K_UP]:
                 
                tempY = int(CarlBase2.rect.bottom)  
                if not JumpHappened2:
                    CarlBase2.jumpy = tempY
                    CarlBase2.is_jump = True

                if DuckHappened2:
                    CarlBase2.jumpy = 575

                if CarlBase2.rect.bottom>=CarlBase2.jumpy-100 and CarlBase2.is_jump:
                    CarlBase2.Jump(7,DuckHappened2,player2)

                if CarlBase2.rect.bottom<=CarlBase2.jumpy-100 or (not CarlBase2.is_jump and CarlBase2.rect.bottom<=CarlBase2.jumpy and not DuckHappened2):
                    CarlBase2.is_jump = False
                    CarlBase2.Jump(5,DuckHappened2,player2)

                if CarlBase2.rect.bottom>=CarlBase2.jumpy and CarlBase2.is_jump==False:
                    CarlBase2.is_jump = True
                
                JumpHappened2 = True
                DuckHappened2 = False


            if keys[py.K_RIGHT]:
                print("cool")
                CarlBase2.DashBackCarl(15,DuckHappened2,JumpHappened2,player2)
                carlSprites.draw(screen)
                DuckHappened2 = False
                JumpHappened2 = False


            if keys[py.K_DOWN]:
                tempX = int(CarlBase2.rect.centerx)
                tempY = int(CarlBase2.rect.centery)
                # change from any sprite to duck
                CarlBase2.Duck(tempX,tempY,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = True
                JumpHappened2 = False


            if keys[py.K_LEFT]:
                CarlBase2.DashForwardCarl(15,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                    # change from any sprite to dash forward

            if keys[py.K_8]:
                CarlBase2.Block(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        CarlBase2.Walkcycle(DuckHappened2,JumpHappened2,player2)
                        DuckHappened2 = False
                        JumpHappened2 = False
        
        case 3:
            player2 = True
            MrsCUNTifulSprites2.empty()
            carlSprites2.empty()
            KishaSprites2.empty()
            kishaBase2 = SwitchingKisha(1200,400,player2)
            KishaSprites2.add(kishaBase2)


            if keys[py.K_UP]:
                tempY = int(KishaBase2.rect.bottom)  
                if not JumpHappened2:
                    KishaBase2.jumpy = tempY
                    KishaBase2.is_jump = True

                if DuckHappened2:
                    KishaBase2.jumpy = 575

                if KishaBase2.rect.bottom>=KishaBase2.jumpy-100 and KishaBase2.is_jump:
                    KishaBase2.Jump(7,DuckHappened2,player2)

                if KishaBase2.rect.bottom<=KishaBase2.jumpy-100 or (not KishaBase2.is_jump and KishaBase2.rect.bottom<=KishaBase2.jumpy and not DuckHappened2):
                    KishaBase2.is_jump = False
                    KishaBase2.Jump(5,DuckHappened2,player2)

                if KishaBase2.rect.bottom>=KishaBase2.jumpy and KishaBase2.is_jump==False:
                    KishaBase2.is_jump = True
                
                JumpHappened2 = True
                DuckHappened2 = False


            if keys[py.K_RIGHT]:
                KishaBase2.DashBackKisha(9,DuckHappened2,JumpHappened2,player2)
                KishaSprites.draw(screen)
                DuckHappened2 = False
                JumpHappened2 = False


            if keys[py.K_DOWN]:
                tempX = int(KishaBase2.rect.centerx)
                tempY = int(KishaBase2.rect.centery)
                # change from any sprite to duck
                KishaBase2.Duck(tempX,tempY,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = True
                JumpHappened2 = False


            if keys[py.K_LEFT]:
                KishaBase2.DashForwardKisha(9,DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False
                    # change from any sprite to dash forward

            if keys[py.K_8]:
                KishaBase2.Block(DuckHappened2,JumpHappened2,player2)
                DuckHappened2 = False
                JumpHappened2 = False

            #when player has not clicked button 
            for event in py.event.get():
                if event.type == py.KEYUP:
                    if timeWhenNoButtonPressed <= 100:
                        timeWhenNoButtonPressed += 1
                    if timeWhenNoButtonPressed == 100:
                        KishaBase2.Walkcycle(DuckHappened2,JumpHappened2,player2)
                        DuckHappened2 = False
                        JumpHappened2 = False
            
    # start time
    # if time is larger than 200 then start walk cycle
    selectButtonP1.draw(screen)
    selectButtonP2.draw(screen)
    carlSprites.draw(screen)
    MrsCUNTifulSprites.draw(screen)
    KishaSprites.draw(screen)
    carlSprites2.draw(screen)
    MrsCUNTifulSprites2.draw(screen)
    KishaSprites2.draw(screen)
    selectButtonP1.update()
    selectButtonP2.update()
    carlSprites.update()
    MrsCUNTifulSprites.update()
    KishaSprites.update()
    carlSprites2.update()
    MrsCUNTifulSprites2.update()
    KishaSprites2.update()
    py.display.update()
    sleep(10/1000)

    