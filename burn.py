import time, hashlib

def burn_cpu(duration_in_s):

    endtime = duration_in_s + time.time()

    while time.time() < endtime:
        meaningless = hashlib.sha512()
