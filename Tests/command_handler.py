from ..Modules.Communications import command_handler
from ..Modules.Magnetometer import magnetometerMT
from ..Modules.Magnetorquer import magnetorquerMT
from ..Modules.Gyro import gyroMT
from ..Modules.Accelerometer import accelerometerMT
from ..Modules.Logging import log


# Initializing command_handler
magnetometer = magnetometerMT.magnetometerMT()
magnetorquer = magnetorquerMT.magnetorquerMT()
gyro = gyroMT.gyroMT()
accelerometer = accelerometerMT.accelerometerMT()
log = log.log("log")

handler = command_handler.command_handler(
        magnetometer, magnetorquer, log, gyro, accelerometer)

# Calling it's methods and making sure it returns what it
# needs to return
print(handler.get_magnetometer([]))
