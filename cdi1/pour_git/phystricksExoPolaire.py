from phystricks import *
def ExoPolaire():
	pspict,fig = SinglePicture("ExoPolaire")
	
	O=Point(0,0)
	X=Point(1,0)

	P=Point(sqrt(3),1)
	P.put_mark(0.1,0,"$(\sqrt{3},1)$",automatic_place=(pspict,"W"))
	P.parameters.symbol="none"

	v=Vector(P)
	m=v.center()
	m.parameters.symbol="none"
	m.put_mark(0.3,m.advised_mark_angle,"$l$")

	theta=Angle(X,O,P,r=0.5)
	theta.put_mark(0.3,theta.advised_mark_angle,r"$\theta$")

	pspict.axes.no_numbering()

	pspict.DrawGraphs(P,m,theta,v)
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
