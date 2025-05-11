import os
from datetime import datetime, timedelta
import tarfile

from config import JOURNAL_DIR, LOG_DATE_FORMAT


def create_tar(files: list[str], now: datetime):
    timestamp = datetime.strftime(now, LOG_DATE_FORMAT)
    timestamp = timestamp.replace(":", "_")
    name_tar = f"{timestamp}.tar.gz"
    output_tar = os.path.join(JOURNAL_DIR, name_tar)

    with tarfile.open(output_tar, "w:gz") as tar:
        for file in files:
            path = os.path.join(JOURNAL_DIR, file)
            tar.add(path)


def get_files():
    now = datetime.now()
    files = os.listdir(JOURNAL_DIR)
    logs = filter(lambda f: f.endswith(".txt"), files)
    
    def log5min(log) -> bool:
        timestr, _ = log.split(".txt")
        timestamp = datetime.strptime(timestr, LOG_DATE_FORMAT)
        if timestamp <= now:
            return True
        return False

    archive_logs = list(filter(log5min, logs))
    create_tar(archive_logs, now)

    for log in archive_logs:
        path = os.path.join(JOURNAL_DIR, log)
        print(path)
        os.remove(path)
    

if __name__ == "__main__":
    get_files()

