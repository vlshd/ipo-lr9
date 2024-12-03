from .isCorrectRect import isCorrectRect
from .isCollisionRect import isCollisionRect
from .intersectionAreaRect import intersectionAreaRect

def intersectionAreaMultiRect(rectangles):
    for rect in rectangles:
        if not isCorrectRect(rect):
            raise ValueError("Некорректный прямоугольник")

    total_area = 0

    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            total_area += intersectionAreaRect(rectangles[i], rectangles[j])

    return total_area
