from manim.mobject.mobject import Mobject

def cast_mobject (objs : list) :
    out = []
    for i in objs:
        if isinstance(i, Mobject):
            out.append(i)
        elif isinstance(i, list) :
            out.extend(i)
        else:
            out.append(i.mobject)
    return out

def file (filename : str) :
    with open(filename, 'r') as f:
        return f.read()
