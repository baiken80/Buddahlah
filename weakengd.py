while not Player.IsGhost:
    Spells.CastMagery("Weaken")
    Target.WaitForTarget(10000, True)
    Target.TargetExecute(0x11305)
    Misc.Pause(2000)