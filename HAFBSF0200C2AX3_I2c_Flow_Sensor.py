import pigpio
import time

pi = pigpio.pi()


class Flow_Sensor:
    def __init__(self):
        self.h = 1
        self.i2c = 0x29
        self.flow = 0

    def read_value(self):
        self.device = pi.i2c_open(self.h, self.i2c)
        self.count, self.data = pi.i2c_read_device(self.device, 2)
        pi.i2c_close(self.device)
        self.flow = int.from_bytes(self.data, "big")
        return self.flow

if __name__ == "__main__":
    # for example
    flow = Flow_Sensor()
    while True:
        print(flow.read_value())
        time.sleep(0.3)
