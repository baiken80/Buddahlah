
Player.ChatSay(63, "a Bull Release")
Gumps.WaitForGump(2426193729, 10000)
Gumps.SendAction(2426193729, 2)
Gumps.SendAction(2426193729, 2)
Gumps.SendAction(2426193729, 2)
Spells.CastNecro('Poison Strike')
Target.WaitForTarget(10000,False)
Target.Last()