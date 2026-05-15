import utl
clear()
powers = {}
while True:
	
	if get_ground_type() == Grounds.Grassland and powers == {}:
		powers = utl.till_plant_and_measure_all(Entities.Sunflower)
		max_power = max(powers)
	elif get_ground_type() == Grounds.Soil and powers == {}:
		powers = utl.plant_and_measure_all(Entities.Sunflower)
		max_power = max(powers)

	for i in range(get_world_size()):
		for j in range(get_world_size()):
			current_pos_power = measure()
			if max_power == current_pos_power and can_harvest():
				harvest()
				powers[max_power] -= 1
			if powers[max_power] == 0:
				powers.pop(max_power)
				if powers == {}:
					break
				max_power = max(powers)
			utl.ez_move("r")
		utl.ez_move("u")
		if powers == {}:
			break
	utl.move_00()
  
	# max_powerが2以下になったら植え直す
	# if powers[max_power] <= 2:
	# 	utl.move_00()
	# 	powers = {}
	# 	powers = utl.plant_and_measure_all(Entities.Sunflower)
	# 	max_power = max(powers)