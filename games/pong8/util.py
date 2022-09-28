from typing import Union


# modfied from https://gist.github.com/kylemcdonald/6132fc1c29fd3767691442ba4bc84018
# intersection between line(p1, p2) and line(p3, p4)
def intersectionTest(p1, p2, p3, p4) -> Union[None, tuple[float, float]]:
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return None
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1: # out of range
        return None
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1: # out of range
        return None
    x = x1 + ua * (x2-x1)
    y = y1 + ua * (y2-y1)
    return (x,y)


def dot(v1x, v1y, v2x, v2y):
    return v1x*v2x + v1y*v2y

# project v1 onto v2
def projection(v1x, v1y, v2x, v2y):
    k = dot(v1x, v1y, v2x, v2y) / dot(v2x, v2y, v2x, v2y)
    return (k*v2x, k*v2y)
