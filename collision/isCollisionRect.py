from .isCorrectRect import isCorrectRect

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1): 
       raise ValueError("1й прямоугольник некоректный.") 
    if not isCorrectRect(rect2): 
        raise ValueError("2й прямоугольник некоректный.") 
        
    if rect1[1][0] < rect2[0][0]: 
        return False 
    if rect1[0][0] > rect2[1][0]: 
        return False 
    if rect1[1][1] < rect2[0][1]: 
        return False 
    if rect1[0][1] > rect2[1][1]: 
        return False 
    
    return True
