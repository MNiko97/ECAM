from time import sleep
import sys

n = 100
for i in range(n):
    sys.stdout.write('\r')
    status = i/n * 100
    pad = int(status+1)
    sys.stdout.write("[%-100s] %d%%" % ('='*pad, pad))
    sys.stdout.flush()
    sleep(0.01)