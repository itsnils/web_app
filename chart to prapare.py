import time

def log(value):
    with open("log_error.txt", 'a') as error_log:
        error_log.write((str(time.strftime("%H:%M:%S"))) + " " + value + "\n")






def chart():
    try:
        n = True
        while n == True:
            with open("sensoric_data/flow_sensor.csv", "r") as flow_read:
                for i, line in enumerate(flow_read):
                    if i == 2000: # 35999
                        for suche in line:
                            if suche == "%":
                                print(line)
                                n = False
                                break
    except:
        log("Error in dataread")











chart()
