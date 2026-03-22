"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task
"""


import pygame as py
from SwitchingSprites4CarlP1 import SwitchingCarl
from SwitchingSprites4KishaP1 import SwitchingKisha
from HealthBarP1 import P1HealthBar
from HealthBarP2 import P2HealthBar
from KishaVictory import KishaVpose
from KishaNameTag import KishaName
from CarlNametag import CarlName
from CarlVictory import CarlVictoryPose
from Win import WinLogo
from time import sleep

#intitalizing values
DuckHappened1 = False
JumpHappened1 = False
DuckHappened2 = False
JumpHappened2 = False
P1IsHitting = False
P2IsHitting = False
P1IsBlocking = False
P2IsBlocking = False
P1Win = False
P2Win = False
player2 = True
#collection of all damage taken to either charachter
P1DamageAll = 0
P2DamageAll = 0


#setting display and initializing pygame
py.init()
size = 1500,750
screen = py.display.set_mode(size) 
py.display.set_caption("Lara's comicbook charachters fighting game")

# selecting number 1 means carl
charSelected4Player1 = 1
#selecting number 2 means Kisha
charSelected4Player2 = 2

#making sprite Groups
carlSprites = py.sprite.Group()
kishaSprites = py.sprite.Group()
healthBars = py.sprite.Group()
victory = py.sprite.Group()
#making healthbars and adding them to healthbar sprite groups
healthBar1 = P1HealthBar(300,100)
healthBar2 = P2HealthBar(1190,100)
healthBars.add(healthBar1)
healthBars.add(healthBar2)




    
# seting player 1 to Carl
if charSelected4Player1 == 1:
    # making sure image dose not flip since they are player 1
    player2 = False
    #drawing Carl to screen and adding to his sprite group
    CarlBase = SwitchingCarl(400,400)
    carlSprites.add(CarlBase)
#setting player 2 to Kisha
if charSelected4Player2 == 2:
    #making image flip because is player 2
    player2 = True
    #drawing Kisha to screen and adding to her sprite group
    KishaBase = SwitchingKisha(1200,375,player2)
    kishaSprites.add(KishaBase)


#Loading music and playing each song once
py.mixer.music.load("./music/track1.mp3")
py.mixer.music.queue("./music/track2.mp3")
py.mixer.music.queue("./music/track3.mp3")
py.mixer.music.play(1)


while True:
    #setting backround as image
    if not P1Win and not P2Win:
        backround = py.image.load("./CharSprites/Backround.png")
        backround = py.transform.scale(backround,(1500,750))
        screen.blit(backround,(0,0))
    elif P1Win:
        backroundWin1 = py.image.load("./CharSprites/winscreen4Carl.png")
        backroundWin1 = py.transform.scale(backroundWin1,(1500,750))
        screen.blit(backroundWin1,(0,0))
    elif P2Win:
        backroundWin2 = py.image.load("./CharSprites/winscreen4Kisha.png")
        backroundWin2 = py.transform.scale(backroundWin2,(1500,750))
        screen.blit(backroundWin2,(0,0))

    # collecting all key events
    py.event.pump()
    keys = py.key.get_pressed()

    #code for player 1/Carl
    if charSelected4Player1 == 1:

            # if w key is pressed move player up then down and change sprite to jumping
            if keys[py.K_w]:
                
                # getting the center y value of the rect before moving picture
                tempY = int(CarlBase.rect.bottom) 

                # if player's last move was not a jump and w key is pressed than player is jumping and make the jumpy = tempY
                if not JumpHappened1:
                    CarlBase.jumpy = tempY
                    CarlBase.is_jump = True

                # if player's last move was a duck than set y value to starting y value
                if DuckHappened1:
                    CarlBase.jumpy = 575

                # if the bottom of the rect is below the max jump height and w is pressed than move up
                if CarlBase.rect.bottom>=CarlBase.jumpy-100 and CarlBase.is_jump:
                    CarlBase.Jump(14,DuckHappened1)

                # if the bottom of the rect is above or equal to the max jump height than move down or
                #  if CarlBase.is_jump == flase than move down if no ducking happened
                if CarlBase.rect.bottom<=CarlBase.jumpy-100 or (not CarlBase.is_jump and CarlBase.rect.bottom<=CarlBase.jumpy and not DuckHappened1):
                    #set .is_jump to false because Carl is falling down now
                    CarlBase.is_jump = False
                    CarlBase.Jump(10,DuckHappened1)

                # if Carl completed a jump but jump button is pressed than set is jump to true to make 
                # Carl go up again and restart jump movement
                if CarlBase.rect.bottom>=CarlBase.jumpy and CarlBase.is_jump==False:
                    CarlBase.is_jump = True
                
                #set JumpHappened to True because w key is pressed which makes the last move jump
                JumpHappened1 = True
                #since jump just happened none of these move were the last move so set all bellow to false
                DuckHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False

            #if a key is pressed move carl to the left/ dash back
            if keys[py.K_a]:
                #call function to change look of sprie and move Carl left at speed of 30 pixals each time a-button is pressed
                CarlBase.DashBackCarl(30,DuckHappened1,JumpHappened1)
                #since dash back just happened none of these move were the last move so set all bellow to false
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False

            # if s key pressed than make charachter duck 
            if keys[py.K_s]:
                #getting values of x and y before duck happens
                
                
                # change from any sprite to duck sprite
                CarlBase.Duck()
                # set duck happened to true because player just ducked
                DuckHappened1 = True
                # set rest to false becuse none of these were the last move of the player
                JumpHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False

            # if d-key is pressed than change from any sprite to dash forward and move Carl forward/right
            if keys[py.K_d]:
                #call function to change sprite and move Carl right
                CarlBase.DashForwardCarl(30,DuckHappened1,JumpHappened1)
                #since Carl just dashed that is his last move meaning none of these are so set all to false
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsHitting = False
                P1IsBlocking = False
                    
            #if q-key pressed then block
            if keys[py.K_q]:
                #call function to change sprite to blocking
                CarlBase.Block(DuckHappened1,JumpHappened1)
                #since Carl just blocked none of these moves were last so set to false
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsHitting = False
                #becuse Carl is blocking or just blocked then set P1IsBlocked to True
                P1IsBlocking = True

            #If e-key is pressed than make Carl attack
            if keys[py.K_e]:
                #call function to change sprite to attack sprite
                CarlBase.Attack(DuckHappened1,JumpHappened1)
                #Since Carl is blocking than none of these moves were the last moves so set them to False
                DuckHappened1 = False
                JumpHappened1 = False
                P1IsBlocking = False
                #Since Carl just hit or is hitting than set P1IsHitting to True since that is last move
                P1IsHitting = True

            #If player 2's last move is hitting/attacking and the rect of P1 and P2 are touching 
            # AND P1/carl is not blocking than change any sprite to being hit 4 P1
            if P2IsHitting and KishaBase.rect.colliderect(CarlBase) and P1IsBlocking == False:
                CarlBase.Hit(DuckHappened1,JumpHappened1)
                #If P1/Carl has not already won then lower healthbar
                if P1Win == False:
                    #use return value of function to calculate all damage done to character to lower healthbar's length to corect amount 
                    P1DamageAll = healthBar1.damageTakenP1(P1DamageAll,8)
                
                #since Carl is being hit than that is his last move so set all below to false
                DuckHappened1 = False
                JumpHappened1 = False
                DuckHappened2 = False
                JumpHappened2 = False

            #If all the damage taken by player 1 is equal to or larger than 500
            #(the length of the healthbar) than remove all sprites from the fighting screen and draw victory screen for Kisha
            if P1DamageAll >= 500:
                #set P2 to win since healthbr is empty
                P2Win = True
                #the removing of all fighting sprites
                CarlBase.kill()
                KishaBase.kill()
                healthBar1.kill()
                healthBar2.kill()
                #making all victory screen sprites for Kisha
                victoryPose = KishaVpose(400,400)
                nameTag = KishaName(1000,300)
                winSign = WinLogo(1100,400)
                #adding all winning screen sprites to victory group
                victory.add(winSign)
                victory.add(nameTag)
                victory.add(victoryPose)
                
                

                
        
    # code for player 2/ Kisha
    if charSelected4Player2 == 2:
            #making sure that all sprite images will be flipped when switched by setting player 2 to true
            player2 = True

            #if up arrow key is pressed than change sprite to jumping image while making it move up and down
            if keys[py.K_UP]:
                #tracking y value before moving
                tempY = int(KishaBase.rect.bottom)  
                #if Kisha's last move was not another jump then player is now jumping and make the jumpy = tempY/the starting point
                if not JumpHappened2:
                    KishaBase.jumpy = tempY
                    KishaBase.is_jump = True

                # if Kisha's last move was a duck then set jumpy to 575
                if DuckHappened2:
                    KishaBase.jumpy = 575

                # if the bottom of Kisha's rect is lower than the max value (jumpy-100) and she is jumping tham move her up until that point
                if KishaBase.rect.bottom>=KishaBase.jumpy-100 and KishaBase.is_jump:
                    KishaBase.Jump(14,DuckHappened2,player2)

                #If the bottom of the rect is higher or equal to the max value than make her fall back down
                # or if she is fallong down than move her down to the mon value while she is not 
                if KishaBase.rect.bottom<=KishaBase.jumpy-100 or (not KishaBase.is_jump and KishaBase.rect.bottom<=KishaBase.jumpy and not DuckHappened2):
                    KishaBase.is_jump = False
                    KishaBase.Jump(10,DuckHappened2,player2)

                # if Kisha completed a jump (bottom of rect is at mon value) but jump button is pressed than set is jump to true to make 
                # Kisha go up again and restart jump movement
                if KishaBase.rect.bottom>=KishaBase.jumpy and KishaBase.is_jump==False:
                    KishaBase.is_jump = True
                
                #since Kisha just jumped that is her last move so set that value to true and the to false 
                JumpHappened2 = True
                DuckHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False

            #if right arrow key is pressed than move Kisha to the right/ make her dash back and change sprite to dashing back
            if keys[py.K_RIGHT]:
                KishaBase.DashBackKisha(18,DuckHappened2,JumpHappened2,player2)
                #since Kisha just dashed back that is the last move she has made so set all bellow to false
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False

            #if down arrow key is pressed make Kisha Duch and change sprite to duck movement
            if keys[py.K_DOWN]:
                # change from any sprite to duck by calling function
                KishaBase.Duck(DuckHappened2,JumpHappened2,player2)
                #since Kisha just ducked set DuckHappened2 to true and all others to false
                DuckHappened2 = True
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False

            #if left arrow key if pressed then make Kisha dash forward and change sprite to dash forward movemenet 
            if keys[py.K_LEFT]:
                #call function to achive this
                KishaBase.DashForwardKisha(18,DuckHappened2,JumpHappened2,player2)
                #since she has dashed or is dashing than none of the bellow has just happened so set them all to false 
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = False

            #when zero button is pressed than make kisha block 
            if keys[py.K_0]:
                #calling function to change sprite to block image
                KishaBase.Block(DuckHappened2,JumpHappened2,player2)
                #set P2 is blocking to true because Kisha is blocking and all else to false 
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = True
                P2IsHitting = False

            #when 8 key is being presed than make Kisha attack
            if keys[py.K_8]:
                #calling function to change sprite to attack sprite
                KishaBase.Attack(DuckHappened2,JumpHappened2,player2)
                #set P2IsHitting to true because Kisha is hitting or her last move is attacking and all else to false
                DuckHappened2 = False
                JumpHappened2 = False
                P2IsBlocking = False
                P2IsHitting = True


            #If Carl is hitting and his rect is touching Kisha while she is not blocking than change her sprite to being hit
            if P1IsHitting and CarlBase.rect.colliderect(KishaBase) and P2IsBlocking == False:
                #call function to change sprite image to being hit
                KishaBase.Hit(DuckHappened2,JumpHappened2,player2)
                # If Kisha has not already won then lower healthbar
                if P2Win == False:
                    #use return value of function to calculate all damage done to character to lower healthbar's length to corect amount 
                    P2DamageAll = healthBar2.damageTakenP2(P2DamageAll,5)

                #since Kisha is being hit than that is her last move so set all below to false
                DuckHappened1 = False
                JumpHappened1 = False
                DuckHappened2 = False
                JumpHappened2 = False

            #if all damage done to Kisha is greater than 500(the length of the healtbar) than put up victory screen for P1/Carl
            if P2DamageAll >= 500:
                #set P1Win as True since Kisha has no health
                P1Win = True
                #remove all fighting sprites from screen 
                CarlBase.kill()
                KishaBase.kill()
                healthBar1.kill()
                healthBar2.kill()
                #add all victory sprites for Carl to the victory sprite group
                victoryPose = CarlVictoryPose(1200,400)
                nameTag = CarlName(500,300)
                winSign = WinLogo(400,400)
                victory.add(winSign)
                victory.add(nameTag)
                victory.add(victoryPose)
                

    #draw all sprites to the screen
    carlSprites.draw(screen)
    kishaSprites.draw(screen)
    healthBars.draw(screen)
    victory.draw(screen)
    #update all sprite groups and display
    carlSprites.update()
    kishaSprites.update()
    healthBars.update()
    victory.update()
    py.display.update()
    #make program wait/sleep to allow display to be shown
    sleep(10/1000)