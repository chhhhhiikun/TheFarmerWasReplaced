import utl
clear()

previous_not_swap_y = 0
previous_not_swap_x = 0
min_previous_not_swap = 0

while True:
	if get_ground_type() == Grounds.Grassland:
		utl.till_and_plant_all(Entities.Cactus)
	else:
		utl.plant_all(Entities.Cactus)  
	min_previous_not_swap = 0
 
	while True:
	
		not_swap_x = 0
		not_swap_y = 0
		not_swap_line_x = 0
		not_swap_line_y = 0
	
		for i in range((get_world_size() - 1) - min_previous_not_swap):
			for i in range(get_world_size()):   
				s = measure()   
				ds = measure(North) 
				if s > ds:  
					swap(North) 
					not_swap_y = 0
				else:
					not_swap_y += 1
				utl.ez_move("r")
			utl.ez_move("u")
			if not_swap_y == get_world_size():
				not_swap_line_y += 1
			else:
				not_swap_line_y = 0
			not_swap_y = 0
		utl.move_00()
	
		for i in range((get_world_size() - 1) - min_previous_not_swap):       
			for i in range(get_world_size()):   
				s = measure()   
				ds = measure(East)  
				if s > ds:  
					swap(East)
					not_swap_x = 0
				else:
					not_swap_x += 1
				utl.ez_move("u")    
			utl.ez_move("r")  
			if not_swap_x == get_world_size():
				not_swap_line_x += 1
			else:
				not_swap_line_x = 0
			not_swap_x = 0
		utl.move_00()
	
		previous_not_swap_x = not_swap_line_x
		previous_not_swap_y = not_swap_line_y
	
		min_previous_not_swap = min_previous_not_swap + min(previous_not_swap_x, previous_not_swap_y)
	
		if min_previous_not_swap == 21:
			utl.move_xy(get_world_size() - 1, get_world_size() - 1)
			harvest()
			utl.move_00()
			break