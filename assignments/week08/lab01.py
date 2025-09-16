"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
    
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def getArea(self):
        self.__area = self.__length * self.__width
        return self.__area
    
    def getPerimeter(self):
        self.__perimeter = (self.__length * 2) + (self.__width * 2)
        return self.__perimeter
    
    def isSquare(self):
        if self.__length != self.__width:
            return f"It is Square"
        else :
            return f"It is Rectangle"
        
A1 = Rectangle(5,5)
print(A1.getArea())
print(A1.getPerimeter())
print(A1.isSquare())
