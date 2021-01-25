import stddraw,math

# x = (R+r)*cos(t) - (r+a)*cos(((R+r)*t)/r)
# y = (R+r)*sin(t) - (r+a)*sin(((R+r)*t)/r)

stddraw.setYscale(-300,300)
stddraw.setXscale(-300,300)
stddraw.setPenRadius(0.0)
stddraw.setPenColor(stddraw.BLUE)

R=int(input("R="))
r=int(input("r="))
a=int(input("a="))


t=0
while True:

    x=(R+r)*math.cos(t) - (r+a)*math.cos(((R+r)*t)/r)
    y=(R+r)*math.sin(t) - (r+a)*math.sin(((R+r)*t)/r)
    stddraw.point(x,y)
    t+=0.01

    stddraw.show(10)










