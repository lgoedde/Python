#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-04 18:02:27 -0400 (Sun, 04 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab06/ip_detect.py $
#$Revision: 82407 $

import re
import sys
import os

def ip_detect(file):
    if not os.access(file,os.R_OK):
        print('Error: Could not read {}'.format(file))
        exit()

    with open(file, 'r') as f:
        data = f.readlines()

    expr = re.compile("^((00[0-9]|0[1-9][0-9]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(00[0-9]|0[1-9][0-9]|[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")

    for item in data:
        item = item.strip()
        ip = item.split(':')[0]
        port = item.split(':')[1]
        #check for those pesky chars in a port...who would put an s in a port...
        try:
            port = int(port)
        except:
            port = 0

        test = re.match(expr,ip)
        if test:
            if port in range(1025,32768):
                print('{} - Valid'.format(item))

            elif port in range(1,1025):
                print('{} - Valid (root privileges required)'.format(item))

            else:
                print('{} - Invalid Port Number'.format(item))

        else:
            print('{} - Invalid IP Address'.format(item))



if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print('Usage: ip_detect.py [filename.in]')
        exit()

    file = sys.argv[1]

    ip_detect(file)

