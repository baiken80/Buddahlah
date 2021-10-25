# This script will run UNTIL you stop it. If you hotkey it, think of it as an on/off switch.
# Add the serials of pets you want to heal to the petList
from System.Collections.Generic import List
from System import Byte
import sys

#Pet list you can add to it by putting the mobileID number in the list. 
petList = [
# PetList
 0x000B67AC, # magare
]


petfilter = Mobiles.Filter()
petfilter.Enabled = True
petfilter.RangeMax = 15
petfilter.IsHuman = False
petfilter.IsGhost = False
petfilter.Serials = List[int] (petList)

while Player.IsGhost == False: 
    
    petList = Mobiles.ApplyFilter(petfilter)   
    for g in petList:
        g = Mobiles.Select(petList, 'Weakest')
        
        #bandage        
        #check health level if in range one of guilded meta pet heals with bandages.          
        if g.Hits < 1:
                bandages = Items.FindByID( 0x0E21, -1, Player.Backpack.Serial )
if bandages != None:
    Items.UseItem( bandages )
    Target.WaitForTarget( 2000, False )
    Target.TargetExecute(g)
else:
    Player.HeadMessage(  'Out of bandages!' )
        
       
    Misc.Pause(50)
Target.ClearLastandQueue()
Target.Cancel() 