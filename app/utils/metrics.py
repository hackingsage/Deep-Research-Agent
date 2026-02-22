import time

def start_timer():
    return time.time()

def end_timer(start):
    return round(time.time() - start, 2)