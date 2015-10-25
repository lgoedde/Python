#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-20 17:07:40 -0400 (Tue, 20 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Lab07/Registration.py $
#$Revision: 82832 $


class Course:

    def __init__(self,courseID,fst,snd,final):
        self.courseID = courseID
        self.fst = fst
        self.snd = snd
        self.final = final
        self.total = 0.25 * self.fst + 0.25 * self.snd + 0.5 * self.final
        self.letter = self.getLetterGrade()

    def __str__(self):
        rstr = '{0}: ({1:.2f}, {2:.2f}, {3:.2f}) = ({4:.2f}, {5})'.format(self.courseID,self.fst,self.snd,self.final,self.total,self.letter)

        return rstr

    def getLetterGrade(self):
        if self.total >= 90:
            return 'A'
        elif self.total >= 80:
            return 'B'
        elif self.total >=70:
            return 'C'
        elif self.total >=60:
            return 'D'
        else:
            return 'F'

class Student:

    def __init__(self,name):
        self.name = name
        self.courses = {}

    def addCourse(self,course):
        if course.courseID in self.courses:
            self.courses.update({course.courseID:course})
        else:
            self.courses.update({course.courseID:course})

    def __str__(self):
        rstr = ''
        rstr += '{}: '.format(self.name)
        tmplist = sorted(self.courses)
        for ind,course in enumerate(tmplist):
            if ind == len(tmplist) - 1:
                rstr += '({}: {})'.format(self.courses[course].courseID,self.courses[course].letter)
            else:
                rstr += '({}: {}), '.format(self.courses[course].courseID,self.courses[course].letter)
        return rstr

    def generateTranscript(self):
        rstr = ''
        rstr += '{}\n'.format(self.name)

        tmplist = sorted(self.courses)
        for ind,course in enumerate(tmplist):
            if ind == len(tmplist) - 1:
                item = self.courses[course]
                rstr += '{0}: ({1:.2f}, {2:.2f}, {3:.2f}) = ({4:.2f}, {5})'.format(item.courseID,item.fst,item.snd,item.final,item.total,item.letter)
            else:
                item = self.courses[course]
                rstr += '{0}: ({1:.2f}, {2:.2f}, {3:.2f}) = ({4:.2f}, {5})\n'.format(item.courseID,item.fst,item.snd,item.final,item.total,item.letter)
        return rstr

class School:

    def __init__(self,name):
        self.name = name
        self.students = {}

    def __str__(self):
        rstr = ''
        rstr += '{}: {} Students\n'.format(self.name,len(self.students))
        tmplist = sorted(self.students)

        for ind,student in enumerate(tmplist):
            if ind == len(tmplist) - 1:
                rstr += '{}'.format(student)
            else:
                rstr += '{}\n'.format(student)

        return rstr

    def loadData(self,filename):
        with open(filename,'r') as f:
            data = f.read()

        data = data.split('\n\n')

        for item in data:
            item = item.split('\n')
            stuname = item[0]
            item.remove(stuname)
            item.remove('--------------------')
            #print(item)
            newStudent = Student(stuname)
            for part in item:
                part = part.strip()
                #print(part)
                exams = part.split(': ')[1]
                exam1 = int(exams.split(',')[0])
                exam2 = int(exams.split(', ')[1])
                final = int(exams.split(', ')[2])
                cid = part.split(':')[0]
                newCourse = Course(cid,exam1,exam2,final)

                newStudent.addCourse(newCourse)

            self.students.update({stuname:newStudent})




    def saveData(self,filename):
        with open(filename, 'a') as f:
            tmplist = sorted(self.students)

            for ind,student in enumerate(tmplist):
                if ind == len(tmplist) - 1:
                    rstr = self.students[student].generateTranscript()
                else:
                    rstr = self.students[student].generateTranscript() + '\n\n'

                f.write(rstr)

if __name__ == "__main__":
    mycourse = Course('ECE364',70.25,80.5,91.3)
    c1 = Course("ECE264", 99, 72, 74)
    c2 = Course("ECE638", 89, 86, 79)
    c3 = Course("ECE464", 96, 90, 67)
    c4 = Course("ECE337", 64, 86, 79)

    student = Student("Margaret Cook")

    for course in [c1, c2, c3, c4]:
        student.addCourse(course)

    string = student.generateTranscript()