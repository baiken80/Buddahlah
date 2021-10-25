if not Player.BuffsExist('Invisibility'):
    Misc.ScriptRun('Discotrainer.py')
    Misc.Pause(5000)


if Player.BuffsExist('Invisibility'):
    Misc.Pause(25000)
    Misc.ScriptRun('Discotrainer.py')    