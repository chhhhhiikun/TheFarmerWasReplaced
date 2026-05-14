import utl
clear()

w = get_world_size()

# (x=奇数 and y=奇数) or (x=偶数 and y=偶数)のときに木を植える
for i in range(w):
	for i in range(w):
		if (not utl.is_even(get_pos_x()) and not utl.is_even(get_pos_y())) or utl.is_even(get_pos_x()) and utl.is_even(get_pos_y()):
			plant(Entities.Tree)
		utl.ez_move("r")
	utl.ez_move("u")	

while True:
	utl.harvest_plant_and_move_v2()