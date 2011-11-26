from phystricks import *
def IntBoutCercle():
    pspict,fig = SinglePicture("IntBoutCercle")

    C=Point(0,0.5)
    alpha=0
    circle = Circle(C,0.5)

    c1=circle.graph(-90,alpha)
    c2=circle.graph(alpha,270)
    c1.parameters.color="red"
    c2.parameters.color="blue"
    P=circle.get_point(alpha)
    P.put_mark(0.3,-45,"$P$")

    s1=Segment(Point(0,0),P)
    segment=s1.dilatation(2)
    segment.parameters.color="red"

    surface=SurfaceBetweenParametricCurves( (s1,0,s1.length()) , (circle,-pi/2,radian(alpha)) )
    surface.parameters.color="cyan"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.curve2.parameters=surface.curve1.parameters

    pspict.DrawGraphs(c1,c2,surface,segment,P)
    pspict.DrawDefaultAxes()
    pspict.dilatation(2)
    fig.conclude()
    fig.write_the_file()