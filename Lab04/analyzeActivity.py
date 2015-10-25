#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-09-22 17:39:41 -0400 (Tue, 22 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab04/analyzeActivity.py $
#$Revision: 82134 $


def getUserPermissions():
    dict = {}
    with open('Permissions.txt','r') as f:
        data = f.readlines()
        del data[0:2]
    for item in data:
        item = item.split(':')
        id = item[0].strip(' ')
        perm =item[1].strip()
        if id not in dict:
            dict.update({'{}'.format(id):[perm]})

        if id in dict:
            dict[id].append(perm)

    for key in dict:
        dict[key] = set(dict[key])

    return dict

def getControllerPermissions():
    dict = {}
    names = {}
    with open('Users.txt', 'r') as f2:
        namedata = f2.readlines()
        del namedata[0:2]

    for item in namedata:
        item = item.split('|')
        id = item[1].strip()
        name = item[0].strip()
        names.update({'{}'.format(id):'{}'.format(name)})


    with open('Permissions.txt','r') as f:
        data = f.readlines()
        del data[0:2]
    for item in data:
        item = item.split(':')
        id = item[0].strip(' ')
        perm =item[1].strip()
        if perm not in dict:
            name = names[id]
            dict.update({'{}'.format(perm):[name]})
        if perm in dict:
            name = names[id]
            dict[perm].append(name)

    for key in dict:
        dict[key] = set(dict[key])

    return dict

def getControllerActions():
    dict = {}
    with open('ActivityLog.txt','r') as f:
        data = f.readlines()

    for item in data:
        item = item.split('/')
        #print(item)
        cont = item[3]
        act = item[4].strip()
        #print(cont,act)

        if cont not in dict:
            dict.update({'{}'.format(cont): [act]})

        if cont in dict:
            dict[cont].append(act)

    for key in dict:
        dict[key] = set(dict[key])
        
    return dict

def parseLogFile():
    #actions = getControllerActions()
    #cperms = getControllerPermissions()
    uperms = getUserPermissions()
    rlist = []
    with open('ActivityLog.txt','r') as f:
        data = f.readlines()

    for item in data:
            item = item.split(':',1)
            id = item[0].strip()
            url = item[1].strip()
            cont = item[1].split('/')[3]
            act = item[1].split('/')[4].strip()

            if id in uperms:
                if cont in uperms[id]:
                    check = True

            else:
                check = False

            rlist.append((id,url,cont,act,check))


    return rlist

def canGrantAccess(userID, url):
    uperms = getUserPermissions()

    if userID not in uperms:
        return False

    cont = url.split('/')[3].strip()

    if cont in uperms[userID]:
        return True
    else:
        return False

def checkUserActivity(userID):
    rlist = []
    uperms = getUserPermissions()
    if userID not in uperms:
        return []

    with open('ActivityLog.txt','r') as f:
        data = f.readlines()

    for item in data:
        item = item.split(':',1)
        url = item[1].strip()

        id = str(item[0].strip())
        if id == userID:
            check = canGrantAccess(userID,url)
            if check == True:
                rlist.append((url,check))

            else:
                rlist.append((url,check))

    return rlist

def getActivityByUser():
    names = {}
    dict = {}

    with open('Users.txt', 'r') as f2:
        namedata = f2.readlines()
        del namedata[0:2]

    for item in namedata:
        item = item.split('|')
        id = item[1].strip()
        name = item[0].strip()
        names.update({'{}'.format(id):'{}'.format(name)})

    with open("ActivityLog.txt", 'r') as f:
        data = f.readlines()

    for item in data:
        item = item.split(':',1)
        url = item[1].strip()
        id = item[0].strip()

        check = canGrantAccess(id,url)
        if names[id] not in dict:
            if check == True:
                dict.update({'{}'.format(names[id]): (1,0)})
            else:
                dict.update({'{}'.format(names[id]): (0,1)})

        if names[id] in dict:
            for (a,b) in dict[names[id]]:
                if check == True:
                    a +=1

                else:
                    b+= 1

    return dict

def getActivityByController():
    data = parseLogFile()
    dict = {}
    for item in data:
        name = str(item[2].strip())
        if name not in dict:
            if item[4] == True:
                dict.update({'{}'.format(name): (1,0)})
            else:
                dict.update({'{}'.format(name): (0,1)})

        else:
            print(dict[name])
            for (t,f) in name:
                if item[4] == True:
                    t+= 1
                else:
                    f+= 1
    print(dict)
    return dict


if __name__ == "__main__":
    getActivityByController()