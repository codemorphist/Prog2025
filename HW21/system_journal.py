from datetime import datetime
import random
import time
import os

from config import JOURNAL_DIR, LOG_DATE_FORMAT



def write_log():
    timestamp = datetime.now().strftime(LOG_DATE_FORMAT)
    log_file = os.path.join(JOURNAL_DIR, f"{timestamp}.txt")
    with open(log_file, "w") as f:
        for _ in range(random.randint(1, 10)):
            f.write(f"[INFO] Some log :: {datetime.now().strftime('%s')}\n")
    print(f"[+] NEW LOG: {log_file}")


def main():
    print("== SYSTEM JOURNAL OPENED ==")
    while True:
        try:
            write_log()
            time.sleep(1.3)
        except KeyboardInterrupt:
            print("== SYSTEM JOURNAL CLOSE ==")
            return


if __name__ == "__main__":
    main()
