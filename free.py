import utl
clear()

#全体に植える
utl.plant_all(Entities.Bush)

#収穫→植える
while True:
	utl.harvest_plant_and_move(Entities.Bush)