import math


#calculate functions:

#hypotenuse

def cal_hyp(side_a, side_b):
	hypotenuse = math.sqrt((side_a * side_a) + (side_b * side_b))
	return (hypotenuse)
	
def cal_side_other(side_a, hypotenuse):
	other_side = math.sqrt((hypotenuse * hypotenuse) - (side_a * side_a))
	return (other_side)

# perimeter
	
def cal_perimeter(sides):
	total = 0
	for a in sides:
		total += a
	return (total)
	
def cal_remaining_perimeter(sides, total_length, total_sides):
	total = 0
	for a in sides:
		total += a
	remaining_length = total_length - total
	remaining_sides = total_sides - len(sides)
	return (remaining_length, remaining_sides)

#circle	

def cal_circumference(radius):
	circumference = math.pi * radius * 2
	return (circumference)
	
def cal_radius(circumference):
	radius = circumference / math.pi / 2
	return (radius)

#area
	
def cal_area_sqr(width):
	area = width * width
	return (area)
	
def cal_area_tri(width, height):
	area = width * height / 2
	return (area)
	
def cal_area_rect(width, height):
	area = width * height
	return (area)	

def cal_area_para(width, height):
	area = width * height
	return (area)
	
def cal_area_kite(width, height):
	area = width * height / 2
	return (area)
	
def cal_area_trap(width_a, width_b, height):
	area = (width_a + width_b) * height / 2
	return (area)
	
def cal_area_circle(radius):
	area = math.pi * (radius * radius)
	return (area)
	
#angles	
			
def cal_angles(angles):
	total = 0
	for a in angles:
		total += a
	return (total)
	
def cal_remaining_angles(angles, sides):
	total = 0
	all_angles = (sides - 2) * 180 
	for a in angles:
		total += a
	remainder = all_angles - total
	remainder_angles = sides - len(angles)
	return (remainder, remainder_angles)

#surface area

def cal_surf_cube(length):
	area = 6 * (length * length)
	return (area)

def cal_surf_cuboid(length, width, height):
	area = 2 * ((length * width) + (length * height) + (width * height))
	return (area)

def cal_surf_prism(length, width, height, slant):
	area = (2 * (width * height / 2)) + (width * length) + (height * length) + (slant * length)
	return (area)

def cal_surf_pyramid(length, slant):
	area = (4 * (length * slant / 2)) + (length * length)
	return (area)
	
def cal_surf_cylinder(radius, height):
	area = (2 * (math.pi * (radius * radius))) + (2 * (math.pi * (radius)) * height)
	return (area)
	
def cal_surf_cone(radius, slant):
	area = (math.pi * radius * slant) + (math.pi * (radius * radius))
	return (area)
	
def cal_surf_sphere(radius):
	area = 4 * (math.pi * (radius * radius))
	return (area)
	
#volume

def cal_volume_cube(length):
	volume = length * length * length
	return (volume)

def cal_volume_cuboid(length, width, height):
	volume = length * width * height
	return (volume)

def cal_volume_prism(length, width, height):
	volume = (length * width * height) / 2
	return (volume)

def cal_volume_cylinder(radius, height):
	volume = (math.pi * (radius * radius)) * height
	return (volume)

def cal_volume_pyramid(length, width, height):
	volume = (length * width * height) / 3
	return (volume)

def cal_volume_cone(radius, height):
	volume = (math.pi * (radius * radius)) * height / 3
	return (volume)

def cal_volume_sphere(radius):
	volume = 4 / 3 * (math.pi * (radius * radius * radius))
	return (volume)

#convert functions:

def convert_radius_diameter(radius):
	diameter = radius * 2
	return (diameter)
	
def convert_diameter_radius(diameter):
	radius = diameter / 2
	return (radius)