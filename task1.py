import math
class point()



p1 = point()

p1.x = 15
p1.y = 20

p2 = point()

p2.x = 25
p2.y = 30

def distance_between_points(p1,p2):
p3 = (p2.x - p1.x)**2
p4 = (p2.y - p1.y)**2

p5 =  p3 + p4
return(math.square(p5))
print distance_between_point(p1,p2)
