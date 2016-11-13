#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-01 17:14:58 -0400 (Tue, 01 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab01/advCalc.bash $
#$Revision: 81283 $

if [[ $# != 1 ]]
then
    echo "Usage: ./advCalc.bash <filename>"
    exit 1
fi

while read line
do
    out=$(./simpleCalc.bash $line)
    if [[ $? != 0 ]]
    then
        echo "$line: Error."
    else
        echo "$line: $out"
    fi
done < $1

exit 0

