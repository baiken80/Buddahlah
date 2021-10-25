enemy = Target.GetTargetFromList('enemy')
if enemy:
    Spells.CastSpellweaving('Word Of Death')
    Target.WaitForTarget(10000,True)
    Target.TargetExecute(enemy)
    Target.TargetExecute(enemy)
    Target.TargetExecute(enemy)
