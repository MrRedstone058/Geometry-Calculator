import math


#calculate functions:

#hypotenuse

def cal_hyp(list):
	side_a, side_b = list[0][0], list[1][0]
	hypotenuse = math.sqrt((side_a * side_a) + (side_b * side_b))
	return (hypotenuse)
	
def cal_side_other(list):
	side_a, hypotenuse = list[0][0], list[1][0]
	other_side = math.sqrt((hypotenuse * hypotenuse) - (side_a * side_a))
	return (other_side)

# perimeter
	
def cal_perimeter(list):
	sides = list[0]
	total = 0
	for a in sides:
		total += a
	return (total)
	
def cal_remaining_perimeter(list):
	sides, total_length, total_sides = list[0], list[1][0], list[2][0]
	total = 0
	for a in sides:
		total += a
	remaining_length = total_length - total
	remaining_sides = total_sides - len(sides)
	return (remaining_length, remaining_sides)

#circle	

def cal_circumference(list):
	radius = list[0][0]
	circumference = math.pi * radius * 2
	return (circumference)
	
def cal_radius(list):
	circumference = list[0][0]
	radius = circumference / math.pi / 2
	return (radius)

#area
	
def cal_area_sqr(list):
	width = list[0][0]
	area = width * width
	return (area)
	
def cal_area_tri(list):
	width, height = list[0][0], list[1][0]
	area = width * height / 2
	return (area)
	
def cal_area_rect(list):
	width, height = list[0][0], list[1][0]
	area = width * height
	return (area)	

def cal_area_para(list):
	width, height = list[0][0], list[1][0]
	area = width * height
	return (area)
	
def cal_area_kite(list):
	width, height = list[0][0], list[1][0]
	area = width * height / 2
	return (area)
	
def cal_area_trap(list):
	width_a, width_b, height = list[0][0], list[1][0], list[2][0]
	area = (width_a + width_b) * height / 2
	return (area)
	
def cal_area_circle(list):
	radius = list[0][0] 
	area = math.pi * (radius * radius)
	return (area)
	
#angles	
			
def cal_angles(list):
	angles = list[0]
	total = 0
	for a in angles:
		total += a
	return (total)
	
def cal_remaining_angles(list):
	angles, sides = list[0], list[1][0]
	total = 0
	all_angles = (sides - 2) * 180 
	for a in angles:
		total += a
	remainder = all_angles - total
	remainder_angles = sides - len(angles)
	return (remainder, remainder_angles)

#surface area

def cal_surf_cube(list):
	length = list[0][0]
	area = 6 * (length * length)
	return (area)

def cal_surf_cuboid(list):
	length, width, height = list[0][0], list[1][0], list[2][0]
	area = 2 * ((length * width) + (length * height) + (width * height))
	return (area)

def cal_surf_prism(list):
	length, width, height, slant
	area = (2 * (width * height / 2)) + (width * length) + (height * length) + (slant * length)
	return (area)

def cal_surf_pyramid(list):
	length, slant = list[0][0], list[1][0]
	area = (4 * (length * slant / 2)) + (length * length)
	return (area)
	
def cal_surf_cylinder(list):
	radius, height = list[0][0], list[1][0]
	area = (2 * (math.pi * (radius * radius))) + (2 * (math.pi * (radius)) * height)
	return (area)
	
def cal_surf_cone(list):
	radius, slant = list[0][0], list[1][0]
	area = (math.pi * radius * slant) + (math.pi * (radius * radius))
	return (area)
	
def cal_surf_sphere(list):
	radius = list[0][0]
	area = 4 * (math.pi * (radius * radius))
	return (area)
	
#volume

def cal_volume_cube(list):
	length = list[0][0]
	volume = length * length * length
	return (volume)

def cal_volume_cuboid(list):
	length, width, height = list[0][0], list[1][0], list[2][0]
	volume = length * width * height
	return (volume)

def cal_volume_prism(list):
	length, width, height = list[0][0], list[1][0], list[2][0]
	volume = (length * width * height) / 2
	return (volume)

def cal_volume_cylinder(list):
	radius, height = list[0][0], list[1][0]
	volume = (math.pi * (radius * radius)) * height
	return (volume)

def cal_volume_pyramid(list):
	length, width, height = list[0][0], list[1][0], list[2][0]
	volume = (length * width * height) / 3
	return (volume)

def cal_volume_cone(list):
	radius, height = list[0][0], list[1][0]
	volume = (math.pi * (radius * radius)) * height / 3
	return (volume)

def cal_volume_sphere(list):
	radius = list[0][0]
	volume = 4 / 3 * (math.pi * (radius * radius * radius))
	return (volume)

#convert functions:

def convert_radius_diameter(list):
	radius = list[0][0]
	diameter = radius * 2
	return (diameter)
	
def convert_diameter_radius(list):
	diameter = list[0][0]
	radius = diameter / 2
	return (radius)
