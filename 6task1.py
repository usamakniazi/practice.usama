import math
class point():
  x=0
  y=0
pnt1=point()
pnt2=point()

def distance_between_points(p1,p2):

 pt1_x=int(input("Enter the value of x co-ordinate of point 1 "))
 pt1_y=int(input("Enter the value of y co-ordinate of point 1 "))
 pt2_x=int(input("Enter the value of x co-ordinate of point 2 "))
 pt2_y=int(input("Enter the value of y co-ordinate of point 2 "))
 p1.x=pt1_x
 p1.y=pt1_y
 p2.x=pt2_x
 p2.y=pt2_y
 print("The first set of points are (%s, %s) "%(p1.x,p1.y))
 print("The second set of points are (%s, %s) "%(p2.x,p2.y))
 first_point=(p1.x,p1.y)
 second_point=(p2.x,p2.y)
 y=dist(first_point,second_point)
 return y

def dist(first,second):
