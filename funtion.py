l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))

def perimeter_rect():
    perimeter=2*(l+b)
    return perimeter
def area_rect():
    area=l*b
    return area
perimeter=perimeter_rect()
print("PERIMETER OF RECTANGLE:",perimeter)
area=area_rect()
print("AREA OF RECTANGLE:",area)
    
