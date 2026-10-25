#ask the user for width and hight
#(assume the put in valid data)
width = float(input("width: "))
height = float(input("height: "))

#caulculate the area/perimeter
area = width * height
perimeter = 2 * (width + height)

#output the area and perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")
