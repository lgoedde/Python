#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-11-03 17:29:38 -0500 (Tue, 03 Nov 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab09/regExPractical.py $
#$Revision: 83141 $

import re

def getNumber(stringInput):
    test = re.compile(r'(\+{0,1}|\-{0,1})[0-9]{1}\.[0-9]+[eE]{1}(\+{0,1}|\-{0,1})[0-9]+')

    check = re.search(test, stringInput)

    if check:
        return check.group()
    else:
        return None

def getOptions(commandLine):
    test = re.compile(r'([\-[a-z]{1}\s*\-]^) | (\-(?P<op>[a-z]{1})\s*(?P<arg>.+))')

    check = re.search(test,commandLine)

    if check:
        #print(check.group())
        print(check.group('op'))
        print(check.group('arg'))

    else:
        print('error')

def getAddressParts(url):
    good = re.compile(r'((http://)|(https://))(?P<base>[a-zA-Z0-9\.]+)/(?P<controller>[a-zA-Z0-9]+)/(?P<action>[a-zA-Z0-9]+)')
    bad = re.compile(r'((http://)|(https://))(?P<base>[a-zA-Z0-9\.]+)/(?P<controller>[[a-zA-Z0-9]+])/(?P<action>[[a-zA-Z0-9]+])')
    check = re.match(good,url)
    check2 = re.match(bad,url)

    if check:
        base = check.group('base')
        controller = check.group('controller')
        action = check.group('action')
        print(base,controller,action)
        return(base,controller,action)



    elif check2:
        return None

def getAttributes(xmlSnippet):
    test = re.compile('(?P<att>[a-z]+)=\"(?P<val>.+)\"')

    check = re.search(test,xmlSnippet)

    if check:
        print(check.group('att'))
        print(check.group('val'))


    else:
        print('error')

