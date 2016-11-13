#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-03 16:31:43 -0400 (Sat, 03 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab05/practical1.py $
#$Revision: 82371 $

def verifySolution(fileName):
    with open(fileName, 'r') as f:
        data = f.readlines()

    newdata = []
    for line in data:
        line = line.strip()
        newline = []
        for item in line:
            newline.append(item)
        newdata.append(newline)
    print(newdata)

    for line in newdata:
        for num in line:
            if line.count(num) > 1:
                return False

    for item in newdata:
        newcols = []
        for i in range(9):
            newcols.append(item[i])

        print(newcols)

    return True

def getCallersOf(phoneNumber):
    namedict = {}
    with open('Students.txt', 'r') as f:
        data = f.readlines()

    del data[0:2]

    for item in data:
        name = item.split('|')[0].strip()
        ext = item.split('|')[1].split('x')[1].strip()

        namedict.update({ext:name})

    with open('Call Log.txt','r') as f:
        data = f.readlines()

    del data[0:2]
    calls = {}
    for item in data:
        cfrom = item.split()[1].split('-')[1]

        todata = item.split('  ')
        for item in todata:
            if item == '':
                todata.remove(item)

        cto = todata[1].strip()


        calls.update({cto:cfrom})

    rlist = []

    for key in calls:
        if phoneNumber == key:
            rlist.append(namedict[calls[phoneNumber]])

    return (rlist)
if __name__ == "__main__":
    getCallerof("(707) 825-5871")

