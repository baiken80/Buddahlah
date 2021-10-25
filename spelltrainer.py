Imoweptimer = 3000
skillTimer = 25000
Timer.Create( 'Imowep' , 1 )
Timer.Create( 'skillTimer' , 1)

Timer.Create('Imowep',Imoweptimer)


          
       
            
            
            
            
            
            
while not Player.IsGhost:
    if not Timer.Check('Imowep') and Player.Mana > 100:
            
            Spells.CastSpellweaving("Wildfire")
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(0x53191)
            Timer.Create( 'Imowep', Imoweptimer )
            Misc.Pause(1000)
          

            while Player.Mana < Player.ManaMax:
                if (not Player.BuffsExist('Meditation') and not Timer.Check('skillTimer')):
                 Player.UseSkill('Meditation')
                 Timer.Check('skillTimer')
                 
                 
                 
                 Misc.Pause(1000)





