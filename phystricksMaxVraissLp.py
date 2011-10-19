from phystricks import *
def MaxVraissLp():
    pspict,fig = SinglePicture("MaxVraissLp")

    x=var('x')
    f=phyFunction(binomial(10,3)*x**3*(1-x)**7).graph(0,1)

    M=f.get_point(0.3)
    Mx=M.projection(pspict.axes.single_axeX)
    l=Segment(M,Mx)
    l.parameters.style="dotted"

    pspict.axes.single_axeX.put_mark(0.3,-90,"$p$")
    pspict.axes.single_axeY.put_mark(0.3,180,"$L(p)$",automatic_place=(pspict,"E"))
    pspict.axes.single_axeX.Dx=0.3
    pspict.axes.single_axeY.Dx=0.2

    pspict.DrawGraphs(M,f,l)
    pspict.DrawDefaultAxes()
    pspict.dilatation(10)
    fig.conclude()
    fig.write_the_file()