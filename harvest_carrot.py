import utl
clear()

for i in range(get_world_size()):
	for i in range(get_world_size()):
		till()
		plant(Entities.Carrot)
		move(East)
	move(North)

while True:
	utl.harvest_plant_and_move_v2()