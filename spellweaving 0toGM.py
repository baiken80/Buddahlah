

while Player.GetSkillValue( 'Spell Weaving' ) < 10:
    Spells.CastSpellweaving('Arcane Circle')  
    Target.WaitForTarget(10000,False)
    Target.SelfQueued()
    Misc.Pause(200)
    
            
                       
while Player.GetSkillValue('Spell Weaving') < 24:
    Spells.CastSpellweaving('Immolating Weapon')  
    Target.WaitForTarget(10000,False)
    Target.SelfQueued()
    Misc.Pause(200)
        
            
while Player.GetSkillValue( 'Spell Weaving' ) < 38:
    Spells.CastSpellweaving('Reaper Form')  
    Target.WaitForTarget(10000,False)
    Target.SelfQueued()
    Misc.Pause(200)
        

while Player.GetSkillValue( 'Spell Weaving' ) < 52:
    Spells.CastSpellweaving('Summon Fiend')  
    Target.WaitForTarget(10000,False)
    Target.SelfQueued()
    Player.ChatSay(1,'An Imp Release')
    Misc.Pause(200)
        
         
        
while Player.GetSkillValue( 'Spell Weaving' ) < 66:
    Spells.CastSpellweaving('Essence of Wind')  
    Target.WaitForTarget(10000,False)
    Target.SelfQueued()
    Misc.Pause(200)
        
while Player.GetSkillValue( 'Spell Weaving' ) < 83:
    Spells.CastSpellweaving('Windfire')  
    Target.WaitForTarget(10000,False)
    Target.SelfQueued()
    Misc.Pause(200)
        
         
while Player.GetSkillValue( 'Spell Weaving' ) < 120:
    if Player.Hits == Player.HitsMax:    
        Spells.CastSpellweaving('Word of Death')  
        Target.WaitForTarget(10000,False)
        Target.SelfQueued()
        Misc.Pause(2000)
    if Player.Hits < Player.HitsMax:
        Spells.CastMagery('Greater Heal')
        Target.WaitForTarget(10000,False)
        Target.SelfQueued()
        Misc.Pause(200)              
            
    while Player.Mana < Player.ManaMax:
        if (not Player.BuffsExist('Meditation')):    
            Player.UseSkill('Meditation')      
            
            


            


            
