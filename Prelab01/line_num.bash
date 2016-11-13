#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-08-26 23:06:21 -0400 (Wed, 26 Aug 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab01/line_num.bash $
#$Revision: 80219 $

if [[ $# != 1 ]]
then
    echo "Please only give one filename at a time!"
    exit 1

elif [[ ! -r $1 ]]
then
    echo "Cannot read $1"
    exit 2

else
    count=1
    while read line
    do
        echo "$count:$line"
        ((count=$count+1))

    done < $1
fi
exit 0
