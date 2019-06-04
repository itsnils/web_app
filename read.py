import time
import datetime
import os

def dateiname():
    return (str(datetime.date.today())+".txt")

print(dateiname())



while True:
    with open(dateiname(), "r") as flow_read:
        line = flow_read.readlines()[-1]
        print(line)
    time.sleep(1)
