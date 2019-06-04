import HAFBSF0200C2AX3_I2c_Flow_Sensor
import time

Flow = HAFBSF0200C2AX3_I2c_Flow_Sensor.Flow_Sensor()


def log(value):
    with open("log_error.txt", 'a') as error_log:
        error_log.write((str(time.strftime("%H:%M:%S"))) + " " + value + "\n")

def read_the_flow():
    try:
        Flow.read_value()
        return Flow.flow
    except:
        log("Error by sensoric: in read the flow")




def delet():
    try:
        with open("sensoric_data/flow_sensor.csv", 'r') as fin:
            data = fin.read().splitlines(True)
        with open("sensoric_data/flow_sensor.csv", 'w') as fout:
            fout.writelines(data[1:])
    except:
        log("Error by sensoric: delet")


while True:
    try:
        flow_write = open("sensoric_data/flow_sensor.csv", "a")
        with open("sensoric_data/flow_sensor.csv", "r") as flow_read:
            flow_count = sum(1 for row in flow_read)
            print(flow_count)
            if flow_count >= 36000:
                delet()
        flow_write.write((str(time.strftime("%H:%M:%S"))) + ";" + (str(read_the_flow()))+"%" + "\n")
    except:
        log("Error by sensoric: write")




    flow_write.close()
    time.sleep(0.1)
