import math

number_sides = int(input('Input number of sides: '))
side_length = float(input('Input the length of a side: '))
area = (number_sides * side_length ** 2) / (4 * math.tan(math.pi / number_sides))
print('The area of the polygon is:', area)