def circle_calculator(r):
    list={"diameter":2*r,"perimeter":2*r*3.14, "area":r*r*3.14}
    
    return list

circle=circle_calculator(4)
print(len(circle))
print(circle["diameter"])
print(circle["perimeter"])
print(circle["area"])
