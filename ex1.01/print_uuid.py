import time
import uuid

s = uuid.uuid4()

while True:
    print(f"{time.strftime('%FT%T')}: {s}", flush=True)
    time.sleep(5)
