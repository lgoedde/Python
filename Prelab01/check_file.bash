#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-08-30 16:48:11 -0400 (Sun, 30 Aug 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab01/check_file.bash $
#$Revision: 80402 $

if [[ $# != 1 ]]
then
    echo "Usage: ./check_file.bash <filename>" 
    exit 1

else
    if [[ -e $1 ]]
    then
        echo "$1 exists"
    else
        echo "$1 does not exist"
    fi

    if [[ -d $1 ]]
    then
        echo "$1 is a directory"
    else
        echo "$1 is not a directory"
    fi

    if [[ -f $1 ]]
    then
        echo "$1 is an ordinary file"
    else
        echo "$1 is not an ordinary file"
    fi

    if [[ -r $1 ]]
    then 
        echo "$1 is readable"
    else
        echo "$1 is not readable"
    fi

    if [[ -w $1 ]]
    then
        echo "$1 is writable"
    else
        echo "$1 is not writable"
    fi

    if [[ -x $1 ]]
    then
        echo "$1 is executable"
    else
        echo "$1 is not executable"
    fi

    exit 0
fi

