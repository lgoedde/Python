#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-01 16:40:51 -0400 (Tue, 01 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab01/getStudentData.bash $
#$Revision: 81247 $

if [[ $# != 1 ]]
then
    echo "Usage: ./getStudentData.bash <course name>"
    exit 1
fi

if [[ $1 != 'ece364' && $1 != 'ece337' ]]
then
    echo "Error: course $1 is not a valid option."
    exit 2
fi

files=$(ls gradebooks/$1*)
numstu=0
total=0
allscores=()
for item in ${files[*]}
do
    scores=$(cat $item | cut -d',' -f2)
    allscores[$numstu]=$scores
    ((numstu=$numstu + $(cat $item | wc -l)))
    
done
max=0

for item in ${allscores[*]}
do
    if [[ $item > $max ]]
    then
        max=$item
    fi
    ((total=$total + $item))
done

for item in ${files[*]}
do
    info=$(cat $item | grep "$max" | cut -d',' -f1)
    if [[ $info == '' ]]
    then 
        continue
    else
        best=$info
    fi    
done
((avg=$total/$numstu))

echo "Total students: $numstu"
echo "Average score: $avg"
echo "$best had the highest score of $max"

exit 0
