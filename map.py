import area as area

rad = [1, 2, 3, 4, 5, 6, 7, 8]
areas = []


def area1():

    for r in rad:
        a=2*3.14*r
        areas.append(a)
    print(areas)
area1()