#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-21 23:59:29 -0400 (Wed, 21 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab08/except.py $
#$Revision: 82876 $

if __name__ == "__main__":
    data = input("Please enter some values: ")
    data = data.split()
    newdata = []
    for item in data:
        try:
            item = float(item)
            newdata.append(item)
        except ValueError:
            pass
            
    print("The sum is: {}".format(sum(newdata)))

