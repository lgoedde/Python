#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2015-10-18 15:41:17 -0400 (Sun, 18 Oct 2015) $
#$HeadURL: svn+ssh://ece364sv@ecegrid/home/ecegrid/a/ece364sv/svn/F15/students/ee364e07/Prelab07/points.py $
#$Revision: 82701 $

class PointND:

    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError("Please enter at least one argument.")

        for num in args:
            if type(num) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")

        self.t = tuple(args)
        self.n = len(args)

    def __str__(self):
        rstr = '('
        for ind,item in enumerate(self.t):
            if ind == len(self.t)-1:
                rstr += '{0:.2f}'.format(item)
            else:
                rstr += '{0:.2f}, '.format(item)
        rstr += ')'
        return rstr

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self,other):
        if other.n != self.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")

        dist = 0
        for ind,item in enumerate(self.t):
            dist += (item - other.t[ind])**2

        dist = (dist)**0.5
        return dist

    def nearestPoint(self,points):
        if len(points) == 0:
            raise ValueError("Input cannot be empty.")

        dist = self.distanceFrom(points[0])
        repnt = points[0]

        for item in points:
            newdist = self.distanceFrom(item)

            if(newdist < dist):
                dist = newdist
                repnt = item

        return repnt

    def clone(self):
        q = PointND(0.0)
        q.t = self.t
        return q

    def __add__(self, other):
        if type(other) == float:
            newcords = []
            rpoint = PointND(0.0)
            for item in self.t:
                newcords.append(item+other)

            rpoint.t = tuple(newcords)
            rpoint.n = len(rpoint.t)
            return rpoint

        else:
            if other.n != self.n:
                raise ValueError("Cannot operate on points with different cardinalities")
            newcords = []
            rpoint = PointND(0.0)
            for ind,item in enumerate(self.t):
                newcords.append(item+other.t[ind])


            rpoint.t = tuple(newcords)
            rpoint.n = len(rpoint.t)
            return rpoint

    __radd__ = __add__

    def __sub__(self, other):
        if type(other) == float:
            newcords = []
            rpoint = PointND(0.0)
            for item in self.t:
                newcords.append(item-other)

            rpoint.t = tuple(newcords)
            rpoint.n = len(rpoint.t)
            return rpoint

        else:
            if other.n != self.n:
                raise ValueError("Cannot operate on points with different cardinalities")
            newcords = []
            rpoint = PointND(0.0)
            for ind,item in enumerate(self.t):
                newcords.append(item-other.t[ind])

            rpoint.t = tuple(newcords)
            rpoint.n = len(rpoint.t)
            return rpoint

    def __mul__(self, other):
        newcords = []
        rpoint = PointND(0.0)
        for item in self.t:
            newcords.append(item*other)

        rpoint.t = tuple(newcords)
        rpoint.n = len(rpoint.t)
        return rpoint

    __rmul__ = __mul__

    def __truediv__(self, other):
        newcords = []
        rpoint = PointND(0.0)
        for item in self.t:
            newcords.append(item/other)

        rpoint.t = tuple(newcords)
        rpoint.n = len(rpoint.t)
        return rpoint

    def __neg__(self):
        newcords = []
        rpoint = PointND(0.0)
        for item in self.t:
            newcords.append(-item)

        rpoint.t = tuple(newcords)
        rpoint.n = len(rpoint.t)
        return rpoint

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        if other.n != self.n:
             raise ValueError("Cannot compare points with different cardinalities.")

        for ind,item in enumerate(self.t):
            if not (item == other.t[ind]):
                return False

        return True

    def __ne__(self, other):
        if other.n != self.n:
             raise ValueError("Cannot compare points with different cardinalities.")

        for ind,item in enumerate(self.t):
            if not (item != other.t[ind]):
                return False

        return True

    def __gt__(self, other):
        if other.n != self.n:
             raise ValueError("Cannot compare points with different cardinalities.")
        org = PointND(0.0)
        zeros = [0.0]*self.n
        org.t = tuple(zeros)
        org.n = self.n

        dist1 = self.distanceFrom(org)
        dist2 = other.distanceFrom(org)

        if dist1 > dist2:
            return True

        else:
            return False

    def __ge__(self, other):
        if other.n != self.n:
             raise ValueError("Cannot compare points with different cardinalities.")
        org = PointND(0.0)
        zeros = [0.0]*self.n
        org.t = tuple(zeros)
        org.n = self.n

        dist1 = self.distanceFrom(org)
        dist2 = other.distanceFrom(org)

        if dist1 >= dist2:
            return True

        else:
            return False

    def __lt__(self, other):
        if other.n != self.n:
             raise ValueError("Cannot compare points with different cardinalities.")
        org = PointND(0.0)
        zeros = [0.0]*self.n
        org.t = tuple(zeros)
        org.n = self.n

        dist1 = self.distanceFrom(org)
        dist2 = other.distanceFrom(org)

        if dist1 < dist2:
            return True

        else:
            return False

    def __le__(self, other):
        if other.n != self.n:
             raise ValueError("Cannot compare points with different cardinalities.")
        org = PointND(0.0)
        zeros = [0.0]*self.n
        org.t = tuple(zeros)
        org.n = self.n

        dist1 = self.distanceFrom(org)
        dist2 = other.distanceFrom(org)

        if dist1 >= dist2:
            return True

        else:
            return False

class Point3D(PointND):

    def __init__(self,x=0.0,y=0.0,z=0.0):
        PointND.__init__(self,x,y,z)
        self.x = x
        self.y = y
        self.z = z


class PointSet():

    def __init__(self, **kwargs):
        if len(kwargs) == 0:
            self.points = set()
            self.n = 0

        for key in kwargs:
            if key == 'pointList':
                templist = kwargs['pointList']

                if len(templist) == 0:
                    raise ValueError("\'pointList\' input parameter cannot be empty.")

                self.n = templist[0].n
                for item in templist:
                    if item.n != self.n:
                        raise ValueError("Expecting a point with cardinality {}.".format(self.n))

                self.points = set(templist)

            else:
                raise KeyError("\'pointList\' input parameter not found.")

    def addPoint(self,p):
        if p.n != self.n:
            raise ValueError("Expecting a point with cardinality {}.".format(self.n))

        self.points.add(p)

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        tempts = list(self.points)
        minpts = list(tempts[0].t)
        maxpts = list(tempts[0].t)

        i = 0
        for point in self.points:
            for ind,cord in enumerate(point.t):
                if cord < minpts[ind]:
                    minpts[ind] = cord

                if cord > maxpts[ind]:
                    maxpts[ind] = cord

        rmin = PointND(0.0)
        rmax = PointND(0.0)

        rmin.t = tuple(minpts)
        rmin.n = self.n
        rmax.t = tuple(maxpts)
        rmax.n = self.n

        return (rmin,rmax)

    def computeNearestNeighbors(self,otherPointSet):
        if self.n != otherPointSet.n:
            raise ValueError("Expecting a point with cardinality {}.".format(self.n))
        rlist = []
        for point in self.points:
            close = point.nearestPoint(list(otherPointSet.points))
            app = (point,close)
            app = tuple(app)
            rlist.append(app)

        rlist = sorted(rlist)
        print(rlist)
        return rlist


    def __add__(self, other):
        if other.n != self.n:
            raise ValueError("Expecting a point with cardinality {}.".format(self.n))

        self.points.add(other)

        return(self)

    def __sub__(self, other):
        if other.n != self.n:
            raise ValueError("Expecting a point with cardinality {}.".format(self.n))

        if other in self.points:
            self.points.remove(other)
            return(self)

        else:
            return(self)


    def __contains__(self, item):
        if item in self.points:
            return True
        else:
            return False




if __name__ == "__main__":
    pass



