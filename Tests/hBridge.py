from ..Modules.Magnetorquer.hBridge import hBridge

actuator = hBridge(23, 24, 14, 15)

while True:
    inp = input('Enter direction : ')
    if inp in ('0', '-1', '1'):
        actuator.SetDirection(int(inp))
        pass
    else:
        break
