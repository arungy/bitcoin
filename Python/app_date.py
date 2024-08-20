#!/usr/bin/python

import sys
import time

def main():
    loc_time = time.localtime(time.time())
    loc_time_s  = f"{loc_time.tm_year}/{loc_time.tm_mon}/{loc_time.tm_mday} "
    loc_time_s += f"{loc_time.tm_hour}:{loc_time.tm_min}:{loc_time.tm_sec}"

    print(loc_time_s)

if __name__ == '__main__':
    main()
