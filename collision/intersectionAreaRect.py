from .isCorrectRect import isCorrectRect
from .isCollisionRect import isCollisionRect

def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1) or not isCorrectRect(rect2): 
        raise ValueError("Некорректный прямоугольник.") 
    
    area = 0 
    
    if isCollisionRect(rect1, rect2): 
        x_left = max(rect1[0][0], rect2[0][0]) 
        y_bottom = max(rect1[0][1], rect2[0][1]) 
        x_right = min(rect1[1][0], rect2[1][0]) 
        y_top = min(rect1[1][1], rect2[1][1]) 
        
        area = (x_right - x_left) * (y_top - y_bottom) 
        
    return area
