import utl
clear()

while True:
	if get_ground_type() == Grounds.Grassland:
		utl.till_and_plant_all(Entities.Pumpkin)
	else:
		utl.plant_all(Entities.Pumpkin)
   
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			e = get_entity_type()
			if e == Entities.Dead_Pumpkin:
				harvest()
				plant(Entities.Pumpkin)
			utl.ez_move("r")
		utl.ez_move("u")
	
#作成中
	dead_list_x = []
	dead_list_y = []
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				e = get_entity_type()
				if e == Entities.Dead_Pumpkin:
					harvest()
					plant(Entities.Pumpkin)
					new_e = get_entity_type()
					if new_e == Entities.Dead_Pumpkin:
						dead_list_x.append(get_pos_x())
						dead_list_y.append(get_pos_y())
						print(dead_list_x, dead_list_y)
				utl.ez_move("r")
			utl.ez_move("u")
		if dead_list_x == []:
			break