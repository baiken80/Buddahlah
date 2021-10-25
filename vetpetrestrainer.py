while Player.GetSkillValue('Veterinary') < 100:
    Items.UseItemByID(0x0E21)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x4AF24)
    Misc.Pause(3000)