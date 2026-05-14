import utl
clear()

n = 0

for i in range(get_world_size()):
	for i in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(East)
	move(North)

while True:

	while n < (get_world_size() ** 2 + 10):
		for i in range(get_world_size()):
			e = get_entity_type()
			if e == Entities.Dead_Pumpkin:
				harvest()
				plant(Entities.Pumpkin)
				n = 0
			else:
				n += 1
			utl.ez_move("r")
		utl.ez_move("u")
		
	n = 0
	harvest()
	utl.move_00()
	utl.plant_all(Entities.Pumpkin)