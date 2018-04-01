import time
import threading

class log:
    """This class represents a log file"""

    def __init__(self, file_name):
        """This constructor build a log file based on a file name
        It is usually built in the directory of the main file"""
        
        # Initializg the lock object
        self.lock = threading.Lock()
        
        # Setting the file name
        self.file_name = file_name

        # If the file doesn't exist it, creates it
        f = open(self.file_name, 'w+')
        f.close()

    def write_to_log(self, text):
        """Write to the log file while keeping multithreading safety"""
        with self.lock:
            with open(self.file_name, 'a') as f:
                current_time = time.strftime("%d/%m/%Y-%H:%M:%S")
                f.write(current_time + '|' + text + '\n')

    def read_from_log(self):
        """Read from the log file while keeping multithreading safety"""
        data = None
        with self.lock:    
            with open(self.file_name, 'r') as f:
                data = f.readlines()
        return data
