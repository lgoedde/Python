#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-06 17:25:38 -0400 (Tue, 06 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab06/parseData.py $
#$Revision: 82610 $

import re

def getAllData():
    with open('UserData.txt','r') as f:
        data = f.readlines()

    namefl = re.compile('(?P<fname1>[a-zA-Z]+) (?P<lname1>[a-zA-Z]+)')
    namelf = re.compile('(?P<lname2>[a-zA-Z]+), (?P<fname2>[a-zA-Z]+)')
    #namelf = re.compile('(?P<lf>[a-zA-Z]+,\ [a-zA-Z]+)')
    email = re.compile('([\w_.-0-9]*)@([\w_.-0-9]*)')
    phone = re.compile('(\([0-9]{3}\)\ [0-9]{3}\-[0-9]{4})|([0-9]{3}\-[0-9]{3}\-[0-9]{4})|([0-9]{10})')
    state = re.compile('([a-zA-Z]+|[a-zA-Z]+ [a-zA-Z]+)$')
    info = {}

    for item in data:
        test = re.match(namefl,item)
        test2 = re.match(namelf,item)
        etest = re.search(email,item)
        ptest = re.search(phone,item)
        stest = re.search(state,item)


        if test:
            first = test.group('fname1')
            last = test.group('lname1')
            full = first + ' ' + last
            info.update({full:[]})
            if etest:
                newmail = etest.group()
                info[full].append(newmail)
            if ptest:
                info[full].append(ptest.group())

            if stest:
                info[full].append(stest.group())

        if test2:
            first = test2.group('fname2')
            last = test2.group('lname2')
            full = first + ' ' + last
            info.update({full:[]})
            if etest:
                newmail = etest.group()
                info[full].append(newmail)
            if ptest:
                info[full].append(ptest.group())

            if stest:
                info[full].append(stest.group())

    print(info)
    return info

def getInvalidUsers():
    data = getAllData()
    iusers = []
    for key in data:
        if len(data[key]) == 0:
            iusers.append(key)

    iusers.sort()

    return iusers


def getUsersWithEmails():
    pass

def getValidUsers():
    data = getAllData()
    valid = []

    for key in data:
        if len(data[key]) == 3:
            newset = (key,data[key][0],data[key][1],data[key][2])
            valid.append(newset)

    print(valid)
    valid.sort()
    return valid

if __name__ == "__main__":
    getInvalidUsers()
    getValidUsers()


