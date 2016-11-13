#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-22 11:07:39 -0400 (Thu, 22 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab08/parse.py $
#$Revision: 82877 $

import sys

if  __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: parse.py [filename]")
        exit()

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            data = f.readlines()
    except:
        print("{} is not a readable file.".format(filename))
        exit()

    
    for item in data:
        item = item.split()
        printstr = ''
        nums = []
        for thing in item:
            try:
                thing = int(thing)
                nums.append(thing)
            except:
                printstr += thing
                printstr += ' '

        try:
            avg = sum(nums)/len(nums)
            print("{0:.3f} {1}".format(avg,printstr))
        except:
            print(printstr)








