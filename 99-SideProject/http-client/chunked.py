import time
import sys

for i in range(5):
    print(i, end=' ')
    sys.stdout.flush()
    time.sleep(1)
