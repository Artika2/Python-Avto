import  math

def sguare(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

print(sguare(4))
print(sguare(2.5))