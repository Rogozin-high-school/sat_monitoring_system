# ------------ Import statements
import threading

# ------------ Local import statements
import magnetometer
import log_thread
import config
import log

# ------------ Variables & Objects
log_lock = threading.Lock()
magnetometer_lock = threading.Lock()
magnetometer = magnetometer.magnetometer()
log = log.log()
log_thread = log_thread.log_thread(magnetometer_lock, log_lock, magnetometer, log)

# ------------ main code
# Starting logger thread
log_thread.start()

# Stopping logger thread
log_thread.stop()