import utl
clear()

for i in range(get_world_size() / 2):

	for i in range(get_world_size() / 2):
		plant(Entities.Tree)
		utl.ez_move("r")
		utl.ez_move("r")

	utl.ez_move("l")
	utl.ez_move("u")

	for i in range(get_world_size() / 2):
		plant(Entities.Tree)
		utl.ez_move("l")
		utl.ez_move("l")

	utl.ez_move("r")
	utl.ez_move("u")

while True:
	for i in range(get_world_size()):
		e = get_entity_type()
		harvest()
		plant(e)
		utl.ez_move("r")
	utl.ez_move("u")