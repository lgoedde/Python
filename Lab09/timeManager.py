#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-11-03 17:29:38 -0500 (Tue, 03 Nov 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab09/timeManager.py $
#$Revision: 83141 $

from timeDuration import *
def getTotalDuration(experimentName):
    with open('Experiments.txt', 'r') as f:
        data = f.readlines()

    mydict = {}

    del(data[0:3])

    for line in data:
        line = line.split()
        #print(line)
        exp = line[0]
        time = line[1]
        iter = int(line[2])
        min = int(time.split(':')[0])
        sec = int(time.split(':')[1])

        newD = Duration(min,sec) * iter

        if exp not in mydict:
                mydict.update({exp: newD})

        else:
            val = mydict[exp]
            val = val+ newD
            mydict.update({exp: val})

    print(mydict)
    return mydict[experimentName]

if __name__ == "__main__":
    getTotalDuration('Experiment13')