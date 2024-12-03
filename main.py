from collision.isCorrectRect import isCorrectRect
from collision.isCollisionRect import isCollisionRect
from collision.intersectionAreaRect import intersectionAreaRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect

def main():
    print("Примеры использования isCorrectRect:")
    print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  
    print(isCorrectRect([(-7, 9), (3, 6)]))      
   
    print("Примеры использования isCollisionRect:")
    print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)])) 
    print(isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))               
    print(isCollisionRect([(1, 1), (2, 2)], [(1, 3), (3, 4)]))                
    
    print("Примеры использования intersectionAreaRect:")
    print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))  
    print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))       
   
    print("Примеры использования intersectionAreaMultiRect:")
    rectangles = [
        [(-3, 1), (9, 10)],
        [(-7, 0), (13, 12)],
        [(0, 0), (5, 5)],
        [(2, 2), (7, 7)]
    ]

    print(f"Общая площадь пересечения: {intersectionAreaMultiRect(rectangles)}")

    incorrect_rectangles = [
        [(-3, 1), (9, 10)],
        [(3, 17), (13, 1)]  
    ]
    print(f"Общая площадь пересечения: {intersectionAreaMultiRect(incorrect_rectangles)}")  

if __name__ == "__main__":
    main()
