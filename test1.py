from vpython import *

def MakeCoordAxesAt(ctr=vector(0,0,0),xnum=3,zcolor=color.white,ds=1e-15):
    """
    This function returns a set of coordinate axes and labels.
    ctr = coordinate center in multiples of ds
    (defaults to vector(0,0,0))
    xnum = half-length of each axis in multiples of ds
    (defaults to 3)
    zcolor = axis and label color
    (defaults to color.white)
    ds = order of magnitude in SI units
    (defaults to 1e-15 m)
    axeslist[] = returned list of axes and labels
    
    Ex: refframe = MakeCoordAxesAt(xnum=5) for a macroscopic frame
    Ex: refframe = MakeCoordAxesAt(xnum=1e-15) for a microscopic frame
    """
    axeslist = []
    xaxis = curve()
    xaxis.append(pos=ds*(ctr-vector(xnum,0,0)),color=zcolor)
    xaxis.append(pos=ds*(ctr+vector(xnum,0,0)),color=zcolor)
    yaxis = curve()
    yaxis.append(pos=ds*(ctr-vector(0,xnum,0)),color=zcolor)
    yaxis.append(pos=ds*(ctr+vector(0,xnum,0)),color=zcolor)
    zaxis = curve()
    zaxis.append(pos=ds*(ctr-vector(0,0,xnum)),color=zcolor)
    zaxis.append(pos=ds*(ctr+vector(0,0,xnum)),color=zcolor)
    axeslist.append(xaxis)
    axeslist.append(yaxis)
    axeslist.append(zaxis)
    axeslist.append(label(pos=ds*vector(xnum+ctr.x,0+ctr.y,0+ctr.z),
    text='x',xoffset=10,yoffset=10,color=zcolor,linecolor=zcolor))
    axeslist.append(label(pos=ds*vector(0+ctr.x,xnum+ctr.y,0+ctr.z),
    text='y',xoffset=10,yoffset=10,color=zcolor,linecolor=zcolor))
    axeslist.append(label(pos=ds*vector(0+ctr.x,0+ctr.y,xnum+ctr.z),
    text='z',xoffset=10,yoffset=10,color=zcolor,linecolor=zcolor))
    return axeslist

def ToggleVis(something):
    """
    This function toggles the visibility of an object.
    The object must support the 'visible' attribute.
    something = either a list or another object
    
    Note that None is returned.
    
    Ex: ToggleVis(vr)
    """
    if something.visible == undefined:
        for c in something:
            c.visible = not c.visible
    else:
        something.visible = not something.visible

scene.title = "MandIpy3 Demo"
# scene.waitfor('click')

ref = MakeCoordAxesAt(vector(0,0,0),4,color.white)
scene.waitfor('click')
ToggleVis(ref)
