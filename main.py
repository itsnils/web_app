import squirrel
import HAFBSF0200C2AX3_I2c_Flow_Sensor
import time

flow = HAFBSF0200C2AX3_I2c_Flow_Sensor.Flow_Sensor()

db = squirrel.Database("log/", 1)


while True:
    db.write_in_the_file(str(flow.read_value()-8193),"%")
  # print(db.read_the_last_line())
    time.sleep(0.95)
    db.remove_the_old_file()
