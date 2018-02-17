# ------------ Import statements
import socket

# ------------ Local import statements
from Modules.Magnetometer import magnetometerMT

from Modules.Magnetorquer import magnetorquerMT

from Modules.Logging import log_thread
from Modules.Logging import log

from Modules.Communications import command_handler
from Modules.Communications import communications

from Modules.Accelerometer import accelerometerMT

from Modules.Gyro import gyroMT

from Modules import config

# ------------ Variables & Objects
# Lowest level modules objects
magnetometer = magnetometerMT.magnetometerMT()
magnetorquer = magnetorquerMT.magnetorquerMT()
accelerometer = accelerometerMT.accelerometerMT()
gyro = gyroMT.gyroMT()
log = log.log(config.LOG_FILE_NAME)

# Higher level modules objects
log_thread = log_thread.log_thread(magnetometer, log)
communications_command_handler = command_handler.command_handler(
        magnetometer, magnetorquer, log, gyro, accelerometer)
communications_thread = communications.Communications(
        communications_command_handler)

# ------------ Starting modules
# Starting logging module
log_thread.start()

# Starting communications module
communications_thread.start()

while communications_thread.should_run:
    pass

# ------------- Stopping modules
# Stopping logging module
log_thread.stop()

# Stopping communications module
communications_thread.stop()
