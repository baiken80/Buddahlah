while not Player.IsGhost:
    Spells.CastMagery('Invisibility')
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x170081)
    Misc.Pause(40000)