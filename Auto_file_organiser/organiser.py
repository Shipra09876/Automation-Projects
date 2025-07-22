import time
from watchdog.observers import Observer
from file_handler import MyHandler
import os
import logging

if __name__ == "__main__":
    # Watch the actual Downloads folder
    path = os.path.expanduser("C:/Users/2001k/Downloads")

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()

    logging.info(f"Watching folder: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Stopped watching")

    observer.join()

# panding 
