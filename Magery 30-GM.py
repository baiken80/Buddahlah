#Magery and Eval Trainer v1.0 by FrankC

# What you need:

# 1) A suit with Lower Reagent Cost 100%

# 2) Full Spellbook

# 3) Over 30.0 Magery. Buy it up if you don't have it.


# Once you have those Press Play and go watch It's Always Sunny in Philadelphia. That show is great. 

while True:
    Magery = Player.GetSkillValue('Magery')
    Eval = Player.GetSkillValue('EvalInt')
    if Magery < 20:
        Spells.CastMagery('Harm')
        Target.WaitForTarget(4200,False)
        Target.TargetExecute(Items.FindByID(0x0EFA,-1,-1))
        Misc.Pause(2100)
        
    elif Magery < 43 and Player.Mana > 20:
        Spells.CastMagery('Fireball')
        Target.WaitForTarget(4300,False)
        Target.TargetExecute(Items.FindByID(0x0EFA,-1,-1))
        Misc.Pause(2100)
        
    elif Magery >= 43 and Magery < 55 and Player.Mana > 11:
        Spells.CastMagery('Lightning')
        Target.WaitForTarget(4100,False)
        Target.TargetExecute(Items.FindByID(0x0EFA,-1,-1))
        Misc.Pause(2100)   
   
    elif Magery >= 55 and Magery < 68  and Player.Mana > 40:
        Spells.CastMagery('Paralyze')
        Target.WaitForTarget(4100,False)
        Target.TargetExecute(Items.FindByID(0x0EFA,-1,-1))
        Misc.Pause(3200)  
       
    elif Magery >= 68 and Magery < 82  and Player.Mana > 40:
        Spells.CastMagery('Energy Bolt')
        Target.WaitForTarget(4100,False)
        Target.TargetExecute(Items.FindByID(0x0EFA,-1,-1))
        Misc.Pause(3200)

    elif Magery >= 82 and Magery < 93  and Player.Mana > 40:
        Spells.CastMagery('Flamestrike')
        Target.WaitForTarget(4100,False)
        Target.TargetExecute(Items.FindByID(0x0EFA,-1,-1))
        Misc.Pause(3200) 

    elif Magery >= 93 and Magery != Player.GetSkillCap('Magery') and Player.Mana > 60:
        Spells.CastMagery('Earthquake')
        Misc.Pause(8200)
            
    elif Eval < Player.GetSkillCap('EvalInt') and Magery == Player.GetSkillCap('Magery'):
        Spells.CastMagery('Reactive Armor')
        Misc.Pause(2100) 
   
    elif Magery == Player.GetSkillCap('Magery') and Eval == Player.GetSkillCap('EvalInt'):
        Misc.ScriptStop('Magery and Eval Trainer.py')