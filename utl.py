# u r d l で移動できる
def ez_move(direction):
	if direction == "u":
		move(North)
	elif direction == "r":
		move(East)
	elif direction == "d":
		move(South)
	elif direction == "l":
		move(West)

# 畑全体に entity に指定したものを植える
def plant_all(entity):
	for i in range (get_world_size()):
		for i in range (get_world_size()):
			plant(entity)
			ez_move("r")
		ez_move("u")
  
# 畑全体に entity に指定したものを植える(tillありver)
def till_and_plant_all(entity):
	for i in range (get_world_size()):
		for i in range (get_world_size()):
			till()
			plant(entity)
			measure()
			ez_move("r")
		ez_move("u")

# ひまわり用 powerを図りながら畑全体に entity に指定したものを植える
def till_plant_and_measure_all(entity):
	number_dict = {}
	for i in range (get_world_size()):
		for i in range (get_world_size()):
			till()
			plant(entity)
			measure_number = measure()
			if measure_number in number_dict:
				number_dict[measure_number] += 1
			else:
				number_dict[measure_number] = 1
			ez_move("r")
		ez_move("u")
	return number_dict

# ひまわり用 powerを図りながら植え直す
def plant_and_measure_all(entity):
	number_dict = {}
	for i in range (get_world_size()):
		for i in range (get_world_size()):
			harvest()
			plant(entity)
			measure_number = measure()
			if measure_number in number_dict:
				number_dict[measure_number] += 1
			else:
				number_dict[measure_number] = 1
			ez_move("r")
		ez_move("u")
	return number_dict

# 収穫可能なときに収穫して entity に指定したものを植える（これを使うならv2でいい）
def harvest_plant_and_move(entity):
	if can_harvest():
		harvest()
		plant(entity)
		if get_pos_x() + 1 != get_world_size():
			ez_move("r")
		else:
			ez_move("r")
			ez_move("u")

# 収穫可能なときに収穫して 収穫したものを植える
def harvest_plant_and_move_v2():
	for i in range(get_world_size()):
		if can_harvest():
			e = get_entity_type()
			harvest()
			plant(e)
		ez_move("r")	
	ez_move("u")

# n が偶数なら true を返す
def is_even(n):
	return n % 2 == 0

# pos(0, 0) に移動する
def move_00():
	p = [get_pos_x(), get_pos_y()]
	for i in range(p[0]):
		ez_move("l")
	for i in range(p[1]):
		ez_move("d")
  
# pos (x, y)に移動する
def move_xy(x, y):
	p = [get_pos_x(), get_pos_y()]
	if p[0] < x:
		for i in range(x - p[0]):
			ez_move("r")
	elif p[0] > x:
		for i in range(p[0] - x):
			ez_move("l")
	if p[1] < y:
		for i in range(y - p[1]):
			ez_move("u")
	elif p[1] > y:
		for i in range(p[1] - y):
			ez_move("d")