# This script relys on Bandage_Timer.py, if you do not have it, it will not work
# Add the serials of pets you want to heal to the petList
from System.Collections.Generic import List
from System import Byte
import sys

if Misc.ScriptStatus("Bandage_Timer.py") == False:
     Misc.ScriptRun("Bandage_Timer.py")
   
   
   
   
#Pet list you can add to it by putting the mobileID number in the list. 
petList = [
 0x000B67AC,# Magare
 0x001231DF,# Shmirgel
 0x00078077,# Tumbak
 0x001AFA4D,# Sopol
 0x0015580A,# Ycpo
 0x0028E693,# Crab
 0x000A1896,# Spida
 0x000263C0,# aragog - getold
 0x0014E207,# chicken test
 0x0011DB49,# roddy piper - donovan wolf
 0x000600B6,# TJ
 0x00011305,# Fattso
 0x001FA4BC,# rando mare
]

# quits if you have less than 80 HP
if Player.GetRealSkillValue('Veterinary') < 50:
    Misc.SendMessage('Not enough vet skill, stopping',33)
    sys.exit()
    
healing = None
while True:
    init = 0
    plist = []
    for i in petList:
        healPet = Mobiles.FindBySerial(i)
        if healPet:
            if healPet.Hits != int(0) and Player.InRangeMobile(healPet, int(1.5)):
                plist.append(healPet.Serial)
    for j in plist:
        if init == 0:
            healing = Mobiles.FindBySerial(j)
            init = 1
        healPet = Mobiles.FindBySerial(j)
        if healPet:
            if healPet.Hits <= healing.Hits or healPet.Poisoned:
                healing = Mobiles.FindBySerial(healPet.Serial)
    if healing:
        pet2Heal = Mobiles.FindBySerial(healing.Serial)
        if pet2Heal:
            if (pet2Heal.Hits < int(23) or pet2Heal.Poisoned) and Player.InRangeMobile(pet2Heal, int(1.5)):
                if Misc.ReadSharedValue('bandageDone') == True and Player.Visible:
                    prevTarget = Target.Last()
                    if Target.HasTarget( ) == False:
                        Misc.SendMessage("Healing " + pet2Heal.Name, 33)  
                        Items.UseItemByID(0x0E21, -1)
                        Target.WaitForTarget(1500)
                        Target.TargetExecute(pet2Heal)
                        Misc.Pause(600)
    
    Misc.Pause(10)