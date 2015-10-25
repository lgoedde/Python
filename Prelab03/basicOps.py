#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-09-13 16:28:31 -0400 (Sun, 13 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab03/basicOps.py $
#$Revision: 81774 $

def addNumbers(num):
    return (sum(range(num+1)))

def addMultiplesOf(num):
    return (sum(range(0,1001,num)))

def getNumberFrequency(match):
    match = str(match)

    string = "The value of Pi is 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0 2 8 8 4 1 9 7 1 6 9 3 9 9 3 7 5 1 0 5 8 2 0 9 7 4 9 4 4 5 9 2 3 0 7 8 1 6 4 0 6 2 8 6 2 0 8 9 9 8 6 2 8 0 3 4 8 2 5 3 4 2 1 1 7 0 6 7 9 8 2 1 4 8 0 8 6 5 1 3 2 8 2 3 0 6 6 4 7 0 9 3 8 4 4 6 0 9 5 5 0 5 8 2 2 3 1 7 2 5 3 5 9 4 0 8 1 2 8 4 8 1"
    
    freq = string.count(match)

    return freq

def getDigitalSum(string):
    return (sum(int(i) for i in string.strip()))
    

def getSequenceWithoutDigit(num):

    strList = ["736925233695599303035509581762617623184956190649483967300203776387436934399982",

             "943020914707361894793269276244518656023955905370512897816345542332011497599489",

             "627842432748378803270141867695262118097500640514975588965029300486760520801049",

             "153788541390942453169171998762894127722112946456829486028149318156024967788794",

             "981377721622935943781100444806079767242927624951078415344642915084276452000204",

             "276947069804177583220909702029165734725158290463091035903784297757265172087724",

             "474095226716630600546971638794317119687348468873818665675127929857501636341131"] 

    strList = ''.join(strList)
    maxnum = 0
    num=str(num)
    newStr=strList.split(num)

    for item in newStr:
        if len(item) > maxnum:
            maxnum = len(item)
            outStr=item

    return(outStr)
        
def capitalizeMe(string):
    string=string.title()
    outStr=""
    for item in string.split():
        outStr+= item[:-1] + item[-1].upper() + " "

    return outStr[:-1]

if __name__ == "__main__":
    pass



