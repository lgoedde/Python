#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-01 16:56:17 -0400 (Tue, 01 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab01/simpleCalc.bash $
#$Revision: 81262 $

if [[ $# != 3 ]]
then 
    echo "Usage ./simpleCalc.bash <operator> <operand1> <operand2>"
    exit 1
fi

if [[ $1 != 'add' && $1 != 'sub' && $1 != 'mul' && $1 != 'div' && $1 != 'exp' && $1 != 'mod' ]]
then
    echo "Error: invalid operator."
    exit 2
fi

if [[ $1 == 'add' ]]
then
    ((result=$2 + $3))
    op='+'

elif [[ $1 == 'sub' ]]
then
    ((result=$2 - $3))
    op='-'

elif [[ $1 == 'mul' ]]
then
    ((result=$2 * $3))
    op='*'

elif [[ $1 == 'div' ]]
then
    ((result=$2 / $3))
    op='/'

elif [[ $1 == 'exp' ]]
then
    ((result=$2 ** $3))
    op='^'

else
    ((result=$2 % $3))
    op='%'

fi

echo "$2 $op $3 = $result"
exit 0
