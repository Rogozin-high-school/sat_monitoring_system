# Import statements
import threading
import time

from . import config
from . import log
from . import logger

# This thread will create a log file and update it
class log_thread(threading.Thread):
    """This class represents a new thread that logs magnetometer data to a log file"""
    
    def __init__(self,magnetometer):
        """Initializes the logging thread
        
        Keyword arguments:
        magnetomter -- magnetometer object to read data from
        log -- log object to log to 
        """
        threading.Thread.__init__(self)
        self.should_log = True
        self.magnetometer = magnetometer
        self.log = logger.get_logger()

    def run(self):
        """Loggin code that reads data from a magnetometer and writes it to a log file"""
        while self.should_log:
            try:
                axes = None

                # Reading the axes data
                axes = self.magnetometer.get_axes()
                
                # Writing to the log file
                self.log.write_to_log('X:' + str(axes[0]) + ' Y:' + str(axes[1]) + ' Z:' + str(axes[2]))
                
                time.sleep(config.LOG_INTERVAL_MS/1000.0)
            except KeyboardInterrupt:
                break

    def stop(self):
        """Safely stopping the thread"""
        self.should_log = False
