
if Player.Poisoned:
    Spells.CastMagery('Cure')
    Target.SelfQueued()
else:
  if Player.Hits < 90:
    Spells.CastMagery('Greater Heal')
    Target.SelfQueued()
  else:
      Spells.CastMagery('Greater Heal')
      Target.HasTarget()