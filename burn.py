import time, hashlib

def burn_cpu():
    BURN_TIME = 0.2

    start = time.time()

    while time.time() < start + BURN_TIME:
        # meaningless = hashlib.sha512()
        1 + 2

    return time.time() - start
