disco = 15000
Timer.Create('disco',15000)

while Player.HitsMax == Player.Hits:
    Timer.Check('disco')
    Player.UseSkill("Discordance")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x1F39F4)
    Misc.Pause(30000)