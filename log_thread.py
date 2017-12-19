# Import statements
import threading
import time
import config
import magnetometerMT
import log

# This thread will create a log file and update it
class log_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.should_log = True
        self.magnetometer = magnetometerMT.magnetometerMT()
        self.log = log.log(config.LOG_FILE_NAME)

    def run(self):
        while self.should_log:
            try:
                axes = None

                # Reading the axes data
                axes = self.magnetometer.axes()
                
                # Writing to the log file
                self.log.write_to_log('X:' + str(axes[0]) + ' Y:' + str(axes[1]) + ' Z:' + str(axes[2]))
                
                time.sleep(config.LOG_INTERVAL_MS/1000.0)
            except KeyboardInterrupt:
                break

    def stop(self):
        self.should_log = False
