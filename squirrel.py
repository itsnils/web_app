#! /user/bin/env python3
import time
import os
import datetime
import contextlib

class Database:

    """
    Squirrel performs tasks to cache data in a file. A new file with date will be created every day.
    it can be specified how long the files live. the bottom line of the file can then be reissued.
    -   write_in_the_file   - is for write data in a file. we uses append and a timestamp.
    -   remove_the_old_file - is to delete the file that is in the past.
    -   read_the_last_line  - read the last line of the file.
    -   split_the_line      - split the last line in a list and then in a string.
    """

    def __init__(self, directory_path, day_range):
        self.day_range = day_range              # type: str
        self.directory_path = directory_path    # type: str
        self.input_value = "-9999.99"           # type: str
        self.last_line = None                   # type: int



    def write_in_the_file(self, *value):
        # insert  - is for write data in a file. we uses append and a timestamp.
        with open(self.directory_path + str(datetime.date.today()) + ".txt", 'a') as write_file:
            write_file.write((str(time.strftime("%H:%M:%S"))) + ";" + (str(";".join(value))) + "\n")
        if time.strftime("%H:%M") == "23:59":
            Database.remove_the_old_file(self.day_range)

    def remove_the_old_file(self,):
        # remove  - is to delete the file that is in the past.
        self.data_subtract = datetime.timedelta(days=self.day_range)
        self.data_after = datetime.date.today() - self.data_subtract
        with contextlib.suppress(FileNotFoundError):
            os.remove(self.directory_path + str(self.data_after) + ".txt")

    def read_the_last_line(self):
        # read    - read the last line of the file.
        with open(self.directory_path + str(datetime.date.today()) + ".txt", "r") as read_file:
            self.last_line = read_file.readlines()[-1]
            return self.last_line

    def split_the_line(self, line, pos):
        # split the last line in a list and then in a string
        line = line.split(";")
        return line[pos]

if __name__ == "__main__":
    # for example
    db = Database("log/", 1) # class is initialized and the number of days to be deleted are entered
    while True:
        db.write_in_the_file("0000001", "0000002", "0000003", "0000004")   # data is transferred
        print(db.split_the_line(db.read_the_last_line(), 1))  # output of the data
        time.sleep(1)
