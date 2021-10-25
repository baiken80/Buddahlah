# Simple script to attack a target from a list and set it to last target
# Set up a targeting filter on the Targeting tab named enemy, example here https://imgur.com/a/f9rvEPe
# The example above will target the nearest grey non humanoid non friended mob within 12 tiles.
Misc.ScriptRun('Test_CheckEquippedDurability.py')
# set enemy variable from the targeting list 'enemy' 
enemy = Target.GetTargetFromList('enemy')

# check if there is an enemy, if there is continue
if enemy:
    Player.ChatSay(16,"All Kill")
    Target.WaitForTarget(1500)
    # this will target the enemy variable obtained from the list in the first line
    Target.TargetExecute(enemy)
    
# if no enemies, alert the player with a head message
else:
    Player.HeadMessage(16,"No Enemies")
    
    
Scissors = Items.FindByID(0x0F9F,0x0000,Player.Backpack.Serial,-1)
Doji = Items.FindByID(0x1079,-1,Player.Backpack.Serial)
if True:
    
     
  if Items.BackpackCount(0x1079,-1) > 0:
    
            Items.UseItem(Scissors)
            Target.WaitForTarget(10000,False)
            Target.TargetExecute(Doji)
            Misc.Pause(1100)
            if Player.Weight > 350:
                sys.exit()
                Misc.Pause(10)