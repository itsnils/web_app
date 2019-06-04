import pigpio
import time
import threading


pi = pigpio.pi()
flow = 0

def flow_value():
    try:
        global flow
        device = pi.i2c_open(1, 0x29)
        count, data = pi.i2c_read_device(device, 2)
        pi.i2c_close(device)
        flow = int.from_bytes(data, "big")
        return flow
        time.sleep(1)
    except:
        time.sleep(1)
        print("Error")


def flow_thread():
    t = threading.Thread(wtarget=Flow)
    t.start()

