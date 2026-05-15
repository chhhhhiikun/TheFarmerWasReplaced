import utl
clear()

# if 育っていて腐っているなら植え直す elif 育っていないなら肥料をやる
def be_pumpkin(e):
	while True:
		if e == Entities.Dead_Pumpkin and not can_harvest():
			plant(Entities.Pumpkin)
			e = get_entity_type()
		elif e == Entities.Pumpkin and not can_harvest():
			use_item(Items.Fertilizer)
			e = get_entity_type()
		else:
			break

plant_list_x = []
plant_list_y = []

while True:
	if get_ground_type() == Grounds.Grassland:
		utl.till_and_plant_all(Entities.Pumpkin)
	else:
		utl.plant_all(Entities.Pumpkin)

	# 二周目 植え直した場所を記録しておく
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			e = get_entity_type()
			if e == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				plant_list_x.append(get_pos_x())
				plant_list_y.append(get_pos_y())
			utl.ez_move("r")
		utl.ez_move("u")

	while True:
		# 記録しておいた場所に移動してbe_pumpkin→育ったらリストから削除
		if len(plant_list_x) != 0:
			utl.move_xy(plant_list_x[0], plant_list_y[0])
			e = get_entity_type()
			be_pumpkin(e)
			plant_list_x.pop(0)
			plant_list_y.pop(0)
		# リストが空になったら収穫して最初に戻る
		if len(plant_list_x) == 0:
			harvest()
			utl.move_00()
			plant_list_x = []
			plant_list_y = []
			break	

# 一周 16 * 16で 約38秒