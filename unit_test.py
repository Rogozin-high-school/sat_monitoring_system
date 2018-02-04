import hBridge
import time

device = hBridge.hBridge(29,31,33,35)
device.setOutput(-1)

while True:
    try:
        time.sleep(0.01)
    except KeyboardInterrupt:
        break
