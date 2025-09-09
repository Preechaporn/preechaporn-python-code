"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        pass
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self):
        pass
        return (self.length + self.width) * 2
    
class Circle:
    def __init__(self, redius):
        self.redius = redius

    def get_area(self):
        return 3.14 * self.redius * self.redius
    
    def get_perimeter(self):
        return 2 * 3.14 * self.redius
    

rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30
circ = Circle(10)
print(circ.get_area())       # should print 314
print(circ.get_perimeter())  # should print 62.8