import utl
clear()

powers = utl.till_plant_and_measure_all(Entities.Sunflower)
max_power = max(powers)

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			current_pos_power = measure()
			if max_power == current_pos_power and can_harvest():
				harvest()
				powers[max_power] -= 1
				plant(Entities.Sunflower)
				new_power = measure()
				if new_power in powers:
					powers[new_power] += 1
				else:
					powers[new_power] = 1
			if powers[max_power] == 0:
				powers.pop(max_power)
				max_power = max(powers)
			utl.ez_move("r")
		utl.ez_move("u")
	# max_powerが2以下になったら植え直す
	if powers[max_power] <= 2:
		utl.move_00()
		powers = {}
		powers = utl.plant_and_measure_all(Entities.Sunflower)
		max_power = max(powers)
