"""
Lara Atanasoova

ComicbookCharachterPVPGame/

My final performence task

Date Modified: Thursday, January 22nd, 2026
"""
import pygame as py

"""
The P2HealthBar class draws the healthbar for Player 2 to the screen and modifies it's size based on how much damage has been done to Kisha/Player2
"""
class P2HealthBar(py.sprite.Sprite):
    """
    The initialize function draws the healthbar for player2 at the spot where the inputs of x and y indicate it to
    """
    def __init__(self,x,y):
        super().__init__()
        self.image = py.Surface((500,50),py.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        py.draw.rect(self.image,(0,255,0),py.Rect(10,10,500,50))

    """
    The damageTakenP2 function changes the length of the healthbar depending on how much damage player 2 has taken by
    taking in the total amount of damage done to player 2 and how much damage was just delt as inputs. It adds the 
    newly done damage aka hitDamage to totalDamage and minuses total damage from 500 which is the original length of the healthbar
    and redrawing the healthbar with that new value to make it shorter. After that it is fliped because this is player 2 and the healthbar
    needs to decrease the other way. Then it returns the new value of total damage inorder to repeate the cycle with 
    an updated amount for totaldamge.
    """
    def damageTakenP2(self,totalDamage, hitDamage):
        totalDamage += hitDamage
        newWidth = 500 - totalDamage
        self.image.fill((0,0,0,0))
        py.draw.rect(self.image,(0,255,0),py.Rect(10,10,newWidth,50))
        self.image = py.transform.flip(self.image,True,False)

        return totalDamage