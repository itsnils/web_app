import time

import squirrel


db = squirrel.Database("../log/", 1)

zeit = []
flow = []




def grap_zeit():
    zeit.append(db.split_the_line(db.read_the_last_line(), 0))
    if len(zeit) == 300:
        del zeit[0:1]
    return zeit

def grap_flow():
    flow.append(db.split_the_line(db.read_the_last_line(), 1))
    if len(flow) == 300:
        del flow[0:1]
    return flow


if __name__ == "__main__":
    # for example
    while True:
        value = ",".join(grap_zeit())

        print(value)
        #print(grap_zeit()[0] +",",grap_zeit()[1])
      #  print(str(grap_flow()))
       # print(str(grap_zeit()))
        time.sleep(1)


