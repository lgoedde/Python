#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-09-15 17:17:24 -0400 (Tue, 15 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab03/myOperations.py $
#$Revision: 81910 $


def checkTypes(l):

    if type(l) != list:
        return None

    if len(l) == 0:
        return None
    intcnt=0
    floatcnt=0
    stringcnt=0

    for item in l:
        if type(item) == int:
            intcnt += 1

        elif type(item) == float:
            floatcnt+=1

        elif type(item) == str:
            stringcnt+= 1


    return [intcnt, floatcnt, stringcnt]


def normalizeVector(v):

        if type(v) != list:
            return None

        if len(v) == 0:
            return None

        lsum = sum(v)
        newv = []
        for item in v:
            item = item / lsum
            newv.append(item)

        return newv

def findMedian(v):
    if type(v) != list:
        return None

    if len(v) == 0:
        return None

    for item in v:
        if type(item) != int and type(item) != float:
            return None


    v = sorted(v)

    if len(v) % 2 == 0:

        mid = len(v)/2

        med=(v[int(mid-.5)]+v[int(mid+.5)])/2

    else:
        mid =len(v)/2 + .5
        print(mid)
        med=v[mid]

    return med


def rectifySignal(signal):

    if type(signal) != list:
        return None

    if len(signal) == 0:
        return None

    newsig = []
    for item in signal:
        if item < 0:
            newsig.append(0)
        else:
            newsig.append(item)

    return newsig

def convertToBoolean(num):

    if type(num) != int:
        return None

    if num not in range(255):
        return None

    numbin = bin(num)
    numbin = reversed(numbin)

    rlist=[]
    for item in numbin:
        if item == '0':
            rlist.append(False)

        elif item == '1':
            rlist.append(True)

        else:
            break

    rlist.reverse()
    return rlist

def convertToInteger(boolList):
    if type(boolList) != list:
        return None

    if len(boolList) == 0:
        return None

    for item in boolList:
        if type(item) != bool:
            return None

    boolList.reverse()
    binnum = ''
    for item in boolList:
        if item == True:
            binnum+= '1'

        elif item == False:
            binnum+= '0'

    binnum+='b0'
    binnum = binnum[::-1]
    binnum = int(binnum,2)
    return binnum

def switchNames(nameList):
    if type(nameList) != list:
        return None

    if len(nameList) == 0:
        return None

    newlist=[]
    for item in nameList:
        name=item.split(',')
        first=name[1].split(' ')[1]
        last=name[0]
        newlist.append("{} {}".format(first,last))

    return newlist

def getWeightAverage(data):
    if type(data) != list:
        return None

    if len(data) == 0:
        return None

    total=0
    for item in data:
        weight = item.split(':')[1].split(' ')[1]
        weight = float(weight)
        total=total+weight

    avg=total/len(data)

    return avg












