import os
import time
import traceback

# how often to poll the file for changes
POLL_PERIOD = 0.5


class FileModified:
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.callback = callback

        # store the last time the file was modified at the start
        self.modified_on = os.path.getmtime(file_path)

    def start(self):
        try:
            while True:
                time.sleep(POLL_PERIOD)
                modified = os.path.getmtime(self.file_path)

                # new modification detected, we can call the handling function
                if modified != self.modified_on:
                    self.modified_on = modified
                    if self.callback():
                        break
        except Exception as e:
            print(traceback.format_exc())
