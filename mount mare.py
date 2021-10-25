


PetList = [
0x001AFA4D,
0x001231DF]
petfilter = Mobiles.Filter()
petfilter.Enabled = True
petfilter.RangeMax = 2

PetList = Mobiles.ApplyFilter(petfilter)
g = Mobiles.Select(PetList,'Nearest')

Mobiles.UseMobile(g)