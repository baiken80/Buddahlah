
while not Player.IsGhost:
    Spells.CastMagery("Weaken")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x15580A)
    Misc.Pause(1500)