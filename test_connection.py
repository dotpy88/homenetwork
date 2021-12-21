import SwitchClass

switch = SwitchClass.Switch()

out = switch.ShutInterface(interface='Gi1/0/15')
print(out)

out = switch.NoShutInterface(interface='Gi1/0/15')
print(out)