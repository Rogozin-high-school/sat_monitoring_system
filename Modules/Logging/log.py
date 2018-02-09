import time
import threading

class log:
    def __init__(self, file_name):
        # Initializg the lock object
        self.lock = threading.Lock()
        
        # Setting the file name
        self.file_name = file_name

        # Making sure the log file exists
        f = open(self.file_name, 'w+')
        f.close()

    # Writes data to the log file
    def write_to_log(self, text):
        with self.lock:
            with open(self.file_name, 'a') as f:
                current_time = time.strftime("%d/%m/%Y-%H:%M:%S")
                f.write(current_time + '|' + text + '\n')

    # Returns the logged data in a list, split by lines
    def read_from_log(self):
        data = None
        with self.lock:    
            with open(self.file_name, 'r') as f:
                data = f.readlines()
        return data
