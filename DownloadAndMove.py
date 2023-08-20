import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/suyas/Downloads"
to_dir = "C:/Users/suyas/OneDrive/Desktop/WhiteHat jr/test"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extension=os.path.splitext(event.src_path)
        time.sleep(2)
        for key,value in dir_tree.items():
            if extension in value:
                fileName=os.path.basename(event.src_path)
                path1=from_dir+"/"+fileName
                path2=to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+fileName
                if os.path.exists(path2):
                    print("moving...."+fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    time.sleep(1)
    def on_deleted(self, event):
        print(f"someone deleted a file {event.src_path}")
    def on_modified(self, event):
        print(f"someone modified a file {event.src_path}")
    def on_moved(self, event):
        print(f"someone moved a file {event.src_path}")
    


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()

    