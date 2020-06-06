import sys
from pathlib import *
import fnmatch
from watchdog.observers import Observer
from watchdog.events import *


class Monitor():
    def __init__(self, target_path: str, recursive: bool = False):
        self.path = target_path
        self.recursive = recursive
        self.observer = Observer()
        event_handler = FileEventHandler(self.path)
        self.observer.schedule(event_handler, self.path, self.recursive)
        self.observer.start()
        print("Start monitor " + self.path)
        try:
            while self.observer.is_alive():
                self.observer.join(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, target_path: str):
        super(FileEventHandler, self).__init__()
        self.target_path = target_path

    def on_any_event(self, event):
        # if event.is_directory:
        print("Monitor:\n")
        for file in Path(self.target_path).iterdir():
            # if fnmatch.fnmatch(file, '*.py'):
            print(file)

    # def on_deleted(self, event):
    #     print("Monitor:\n")
    #     for file in Path(self.target_path).iterdir():
    #         # if fnmatch.fnmatch(file, '*.py'):
    #         print(file)

if __name__ == '__main__':
    path = r'C:\Will\LocalGit\SWEN90013-2020-NT\runtime'
    monitor = Monitor(path, False)
