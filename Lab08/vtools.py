#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-27 17:49:08 -0400 (Tue, 27 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab08/vtools.py $
#$Revision: 83047 $

import re


def isValidName(identifier):
    identifier = identifier
    test = re.compile('\w')
    for item in identifier:
        check = re.match(test,item)

        if check:
            pass
        else:
            return False

    return True

def parsePinAssignment(assignment):
    test=re.compile('\.(?P<port>\w+)\((?P<pin>\w+)\)')
    check = re.match(test,assignment)

    if check:
        port = check.group('port')
        pin = check.group('pin')

        if not isValidName(port):
            raise ValueError(assignment)
        if not isValidName(pin):
            raise ValueError(assignment)

    else:
        raise ValueError(assignment)

    return (port, pin)

def parseNetLine(line):
    test = re.compile('\s*(?P<comp>\w+)\s+(?P<inst>\w+)\s*\(\s*(?P<netlist>[\w+\,*\.\(\)\s]+)\)')
    check = re.match(test,line)

    if check:
        comp = check.group('comp')
        inst = check.group('inst')
        netlist = check.group('netlist')
        if not isValidName(comp):
            raise ValueError(line)
        if not isValidName(inst):
            raise ValueError(line)

    else:
        raise ValueError(line)

    #print(netlist)
    #test2 = re.compile('[\)\)]*')
    #check2 = re.match(test2,netlist)

    #if check2:
     #   raise ValueError(line)
    #else:
     #   print('No error')
    mylist = []
    pins = netlist.split(',')
    for i,pin in enumerate(pins):
        pin = pin.strip()
        try:
            (port,pin) = parsePinAssignment(pin)
            mylist.append((port,pin))
        except:
            raise ValueError(pin)

    print(comp,inst,tuple(mylist))
    return tuple((comp,inst,tuple(mylist)))

if __name__ == "__main__":
    mytup = parseNetLine("First U22 (.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25)))")
    print(mytup)