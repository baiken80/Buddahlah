
while not Player.IsGhost:
    tenekie = Items.FindByID(0x1EB8,0x0000,0x43910C32,-1)
    Items.UseItem(tenekie)
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 51)
    Misc.Pause(2000)
    Organizer.FStart()
    Misc.Pause(500)
    Restock.FStart()
    Misc.Pause(500)
    Organizer.FStop()
    if Player.GetSkillStatus('Thinkering')  >= 100:  
        Misc.ScriptStopAll()
    