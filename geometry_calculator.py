import geometryalt
from geometryalt import *
import os as o

def setup():
	global section, text, requirements, answer_types_1, total_ans, funcs, results
	section = 'menu'
	text = {
	'menu': [
	'Welcome to the Geometry calculator!\n', 
	'What would you like to calculate? (Use the keywords highlighted in "")\n', 
	'"a": hypotenuse functions', 
	'"b": perimeter functions', 
	'"c": circle functions', 
	'"d": areas functions', 
	'"e": angles functions', 
	'"f": surface area functions', 
	'"g": volume functions', 
	'"h": conversion functions\n'
	], 
	
	'get_ans': {
	'a': ['"a": calculate hypotenuse', '"b": calculate shorter side'], 
	'b': ['"a": calculate perimeter', '"b": calculate remaining perimeter'],
	'c': ['"a": calculate circumference', '"b": calculate radius'],
	'd': ['"a": calculate area of square', '"b": calculate area of triangle', '"c": calculate area of rectangle', '"d": calculate area of parallelogram', '"e": calculate area of kite', '"f": calculate area of trapezium', '"g": calculate area of circle'],
	'e': ['"a": calculate angles', '"b": calculate remaining angles'],
	'f': ['"a": calculate area of cube', '"b": calculate area of cuboid', '"c": calculate area of prism', '"d": calculate area of cylinder', '"e": calculate area of pyramid', '"f": calculate area of cone', '"g": calculate area of sphere'],
	'g': ['"a": calculate volume of cube', '"b": calculate volume of cuboid', '"c": calculate volume of prism', '"d": calculate volume of cylinder', '"e": calculate volume of pyramid', '"f": calculate volume of cone', '"g": calculate volume of sphere'],
	'h': ['"a": calculate conversion of radius to diameter', '"b": calculate conversion of diameter to radius']
	},
	
	'operation': {
	'a': {'a': 'Enter the length of side a and b:', 'b': 'Enter the length of side a and the hypotenuse:'}, 
	'b': {'a': 'Enter the length of all known sides:', 'b': 'Enter the list of the length of all known sides, the total length of the polygon, and the total number of sides on the polygon:'},
	'c': {'a': 'Enter the radius of the circle:', 'b': 'Enter the circumference of the circle:'},
	'd': {'a': 'Enter the width of the square:', 'b': 'Enter the width and height of the triangle:', 'c': 'Enter the width and height of the rectangle:', 'd': 'Enter the width and height of the parallelogram:', 'e': 'Enter the width and height of the kite:', 'f': 'Enter the first, second width and the height of the trapezium:', 'g': 'Enter the radius of the circle:'},
	'e': {'a': 'Enter the value of all known angles:', 'b': 'Enter the list of the values of all known of the angles and the total sides of the polygon:'},
	'f': {'a': 'Enter the length of the cube:', 'b': 'Enter the length, width, and height of the cuboid:', 'c': 'Enter the length, width, height, and slant of the prism:', 'd': 'Enter the radius and height of the cylinder:', 'e': 'Enter the length and slant of the pyramid:', 'f': 'Enter the radius and slant of the cone:', 'g': 'Enter the radius of the sphere:'},
	'g': {'a': 'Enter the width of the cube:', 'b': 'Enter the length, width, and height of the cuboid:', 'c': 'Enter the length, width, and height of the prism:', 'd': 'Enter the radius and height of the cylinder:', 'e': 'Enter the length, width, and height of the pyramid:', 'f': 'Enter the radius and the height of the cone:', 'g': 'Enter the radius of the sphere:'},
	'h': {'a': 'Enter the radius:', 'b': 'Enter the diameter:'}
	}
	}
	
	requirements = {
	'a': {'a': ['Length of side a: ', 'Length of side b: '], 'b': ['Length of side a: ', 'Length of hypotenuse: ']}, 
	'b': {'a': ['List of all lengths of known sides: '], 'b': ['List of all lengths of known sides: ', 'Total length of the polygon: ', 'Total sides of the polgon: ']},
	'c': {'a': ['Radius of circle: '], 'b': ['Circumference of circle: ']},
	'd': {'a': ['Width of square: '], 'b': ['Width of triangle: ', 'Height of triangle: '], 'c': ['Width of rectangle: ', 'Height of rectangle: '],'d': ['Width of parallelogram: ', 'Height of parallelogram: '],'e': ['Width of kite: ', 'Height of kite: '],'f': ['Width a of trapezium: ', 'Width b of trapezium: ', 'Height of trapezium: '], 'g': ['Radius of circle: ']},
	'e': {'a': ['List of all values of known angles: '], 'b': ['List of all values of known angles: ', 'Total sides of the polygon: ']},
	'f': {'a': ['Length of cube: '], 'b': ['Length of cuboid: ', 'Width of cuboid: ', 'Height of cuboid: '], 'c': ['Length of prism: ', 'Width of prism: ', 'Height of prism: ', 'Slant of prism: '], 'd': ['Radius of cylinder: ', 'Height of cylinder: '], 'e': ['Length of pyramid: ', 'Slant of pyramid: '], 'f': ['Radius of cone: ', 'Slant of cone: '], 'g': ['Radius of sphere: ']},
	'g': {'a': ['Width of cube: '], 'b': ['Length of cuboid: ', 'Width of cuboid: ', 'Height of cuboid: '], 'c': ['Length of prism: ', 'Width of prism: ', 'Height of prism: '], 'd': ['Radius of cylinder: ', 'Height of cylinder: '], 'e': ['Length of pyramid: ', 'Width of pyramid: ', 'Height of pyramid: '], 'f': ['Radius of cone: ', 'Height of cone: '], 'g': ['Radius of sphere: ']},
	'h': {'a': ['Radius: '], 'b': ['Diameter: ']}
	}
	
	answer_types_1 = [[
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
	], {
	'a': ['a', 'b'], 
	'b': ['a', 'b'], 
	'c': ['a', 'b'], 
	'd': ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 
	'e': ['a', 'b'], 
	'f': ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 
	'g': ['a', 'b', 'c', 'd', 'e', 'f', 'g'], 
	'h': ['a', 'b']
	}]
	
	total_ans = {
	'a': {'a': 2, 'b': 2},
	'b': {'a': 1, 'b': 3},
	'c': {'a': 1, 'b': 1},
	'd': {'a': 1, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 3, 'g': 1},
	'e': {'a': 1, 'b': 2},
	'f': {'a': 1, 'b': 3, 'c': 4, 'd': 2, 'e': 2, 'f': 2, 'g': 1},
	'g': {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 3, 'f': 2, 'g': 1},
	'h': {'a': 1, 'b': 1}
	}
	
	funcs = {
	'a': {'a': cal_hyp, 'b': cal_side_other},
	'b': {'a': cal_perimeter, 'b': cal_remaining_perimeter},
	'c': {'a': cal_circumference, 'b': cal_radius},
	'd': {'a': cal_area_sqr, 'b': cal_area_tri, 'c': cal_area_rect, 'd': cal_area_para, 'e': cal_area_kite, 'f': cal_area_trap, 'g': cal_area_circle},
	'e': {'a': cal_angles, 'b': cal_remaining_angles},
	'f': {'a': cal_surf_cube, 'b': cal_surf_cuboid, 'c': cal_surf_prism, 'd': cal_surf_cylinder, 'e': cal_surf_pyramid, 'f': cal_surf_cone, 'g': cal_surf_sphere},
	'g': {'a': cal_volume_cube, 'b': cal_volume_cuboid, 'c': cal_volume_prism, 'd': cal_volume_cylinder, 'e': cal_volume_pyramid, 'f': cal_volume_cone, 'g': cal_volume_sphere},
	'h': {'a': convert_radius_diameter, 'b': convert_diameter_radius}
	}
	
	results = {
	'a': {'a': 'The length of the hypotenuse is:', 'b': 'The length of side b is:'},
	'b': {'a': 'The perimeter of the polygon is:', 'b': 'The remaining length from the total perimeter and the total of undefined sides are:'},
	'c': {'a': 'The circumference of the circle is:', 'b': 'The radius of the circle is:'},
	'd': {'a': 'The area of the square is:', 'b': 'The area of the triangle is:', 'c': 'The area of the rectangle is:', 'd': 'The area of the parallelogram is:', 'e': 'The area of the kite is:', 'f': 'The area of the trapezium is:', 'g': 'The area of the circle is:'},
	'e': {'a': 'The total angle is:', 'b': 'The remaining angles left from the polygon and the total of undefined angles are:'},
	'f': {'a': 'The surface area of the cube is:', 'b': 'The surface area of the cuboid is:', 'c': 'The surface area of the prism is:', 'd': 'The surface area of the cylinder is:', 'e': 'The surface area of the pyramid is:', 'f': 'The surface area of the cone is:', 'g': 'The surface area of the sphere is:'},
	'g': {'a': 'The volume of the cube is:', 'b': 'The volume of the cuboid is:', 'c': 'The volume of the prism is:', 'd': 'The volume of the cylinder is:', 'e': 'The volume of the pyramid is:', 'f': 'The volume of the cone is:', 'g': 'The volume of the sphere is:'},
	'h': {'a': 'The diameter is:', 'b': 'The radius is:'}
	}

def convert_nums(num):
	for number in range(len(num)):
		try:
			num[number] = float(num[number])
		except:
			return('Error')
	return(num)
	
def clear():
	o.system('clear')
	o.system('cls' if o.name == 'nt' else "printf '\033c'")
	
def calculate(ans, ans2, ans3, choices):
	section = 'calculate'
	if len(ans3) == total_ans[ans][ans2]:
		try:
			ans6 = funcs[ans][ans2](ans3)
			print(results[ans][ans2], ans6)
			print('Press "Enter" key to return to menu')
			input()
			clear()
			menu()
		except:
			print('Error while computing, please press "Enter" key to try again')
			input()
			clear()
			get_operation(ans, ans2, choices)

def get_operation(ans, ans2, choices):
	ans2 = ans2.lower()
	section = 'operation'
	print('Note:') 
	print('When entering a value based on an function (eg. Enter the width and height of the object), please give only one input defining the current variable.')
	print('When asked for ((item) of all known (object)), such as (eg. Length of all known sides), please give an input of the values in a list: \n(eg. 24 23.5 67)\n')
	print(text[section][ans][ans2])
	ans3 = []
	for a in range(total_ans[ans][ans2]):
		ans4 = input(requirements[ans][ans2][a]).split()
		ans3.append(ans4)
	ans5 = []
	for a in range(len(ans3)):
		ans5.append(convert_nums(ans3[a]))
	if 'Error' in ans5:
		clear()
		get_operation(ans, ans2, choices)
	else:
		clear()
		calculate(ans, ans2, ans5, choices)
		
def get_ans(ans, choices):
	ans = ans.lower()
	section = 'get_ans'
	print('Choose your option:\n')
	for line in text[section][ans]:
		print(line)	
	ans2 = input()
	if not ans2.isnumeric() and ans2.lower() in choices:
		clear()
		get_operation(ans, ans2, choices)
	else:
		clear()
		get_ans(ans, choices)		
	
def menu():
	for line in text[section]:
		print(line)
		
	ans = input()
	if not ans.isnumeric() and ans.lower() in answer_types_1[0]:
		clear()
		get_ans(ans, answer_types_1[1][ans.lower()])
	else:
		clear()
		menu()
		
if __name__ == '__main__':
	setup()	
	menu()
