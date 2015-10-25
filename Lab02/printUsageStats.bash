#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2015-09-08 16:55:50 -0400 (Tue, 08 Sep 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab02/printUsageStats.bash $
#$Revision: 81681 $

if [[ $# != 1 ]]
then
    echo "Usage: ./printUsageStats.bash <filename>"
    exit 1
fi

if [[ ! -e $1 ]]
then
    echo "$1 does not exist"
    exit 2
fi

tstamp=$(head -1 $1 | cut -d' ' -f3)
echo "Parsing file \"$1\". Timestamp: $tstamp"

cat $1 | tail -n +8 > $1_noheader

echo "Your choices are:"
echo "1) Active user IDs"
echo "2) Highest CPU usage"
echo "3) Top 3 longest running processes"
echo "4) All processes by a specific user"
echo "5) Exit"

while [[ 1 ]]
do 
    echo -n "Please enter your choice: "
    read choice

    if [[ $choice == 1 ]]
    then
        usercount=$(head -1 $1 | cut -d',' -f3 | cut -d' ' -f2)
        echo "Total number of active user IDs: $usercount"

    elif [[ $choice == 2 ]]
    then
        user=$(head -1 $1_noheader | cut -d' ' -f2)
        cpu=$(head -1 $1_noheader | cut -d' ' -f9)
        echo "User $user is utilizing the highest CPU resources at $cpu%"

    elif [[ $choice == 3 ]]
    then
        cat $1_noheader | sort -n -r -k 11 | head -3        

    elif [[ $choice == 4 ]]
    then
        echo -n "Please enter a valid username: "
        read user
        echo -n "Please enter a filename to save the user's processes: "
        read filename

        output=$(cat $1_noheader | grep "$user")
        
        if [[ $output != '' ]]
        then
            echo $output > $filename
            
            echo "Output written to file $filename"
        else
            echo "No match found"
        fi


    elif [[ $choice == 5 ]]
    then
        exit 0

    else
        echo "Invalid option. Please enter a number 1 through 5"
    fi

done


exit 0
