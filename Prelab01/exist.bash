#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-08-26 23:03:53 -0400 (Wed, 26 Aug 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab01/exist.bash $
#$Revision: 80218 $

while (($# != 0))
do
    if [[ -e $1 ]]
    then
        if [[ -r $1 ]]
        then
            echo "File $1 is readable!"
        else
            echo "File $1 is not readable!"
        fi
    else
        touch $1
    fi
    shift
done
exit 0
