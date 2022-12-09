from datetime import datetime
import time


now1 = datetime.now()
print(now1)
time.sleep(2)

now = datetime.now()
print(now)

if now1 < now:
    print("hej")
