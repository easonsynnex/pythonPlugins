import time

from datetime import datetime
from time import sleep

last = datetime.now()

sleep(2)
now = datetime.now()
diff = abs(now - last)
if diff.total_seconds() <= 1:
    print('1秒内')
else:
    print(f'超过1秒 {diff}')