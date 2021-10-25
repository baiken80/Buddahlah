wofdtimer = 3000
skilltimer = 25000
Timer.Create( 'wofd' , 1 )
Timer.Create( 'skilltimer' , 1)

Timer.Create('wofd',wofdtimer)


          
       
            
            
            
            
            
            
while not Player.IsGhost:
    if not Timer.Check('wofd') and Player.Mana > 100 and Player.Hits > 100:
            
            Spells.CastSpellweaving("Word of Death")
            Target.WaitForTarget(10000,False)
            Target.SelfQueued()
            Timer.Create( 'wofd', wofdtimer )
            Misc.Pause(200)
    if Player.Hits < Player.HitsMax:
       Spells.CastMagery('Heal')
       Target.SelfQueued()
       Misc.Pause(2000)      

       while Player.Mana < Player.ManaMax:
                
           if (not Player.BuffsExist('Meditation') and not Timer.Check('skilltimer')):
              Player.UseSkill('Meditation')
              Timer.Check('skilltimer')
                 
                
                    





