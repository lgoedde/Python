#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-11-03 17:29:38 -0500 (Tue, 03 Nov 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab09/timeDuration.py $
#$Revision: 83141 $

class Duration():
    def __init__(self, hours=0,minutes=0,seconds=0):
        if type(hours) != int:
            raise TypeError("This class only accepts integers")
        elif type(minutes) != int:
            raise TypeError("This class only accepts integers")
        elif type(seconds) != int:
            raise TypeError("This class only accepts integers")

        if hours < 0:
            raise ValueError("Values cannot be negative")
        if minutes < 0:
            raise ValueError("Values cannot be negative")
        if seconds < 0:
            raise ValueError("Values cannot be negative")

        if seconds > 60:
            minutes += (seconds // 60)
            seconds = seconds % 60

        if minutes > 60:
            hours += (minutes // 60)
            minutes = minutes % 60



        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        rstr = ''
        rstr += '{}:{}:{}'.format(self.hours,self.minutes,self.seconds)
        return rstr

    def getTotalSeconds(self):
        return (self.hours*3600 + self.minutes*60+self.seconds)

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError("Duration Instance expected")

        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds
        hours = self.hours + other.hours
        myD = Duration(hours,minutes,seconds)
        return myD

    __radd__ = __add__

    def __mul__(self, other):
        if type(other) != int:
            raise TypeError("Expecting an integer")

        if other < 0:
            raise ValueError("Integer must be positive")

        seconds = self.seconds * other
        minutes = self.minutes * other
        hours = self.hours * other

        myD = Duration(hours,minutes,seconds)
        return myD

    __rmul__ = __mul__


if __name__ == "__main__":
    td = Duration(2,125,75)
    print(td)