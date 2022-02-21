from Spec_repo import *

class MySpec(object):
	def __init__(self,colour,istrans):
		self.colour=colour
		self.istrans=istrans


##### Toggle between turing machines and manual tiling #######
STATE_TILES = True
####################### MANUAL SPECS #########################
if not STATE_TILES:
	rows = 80
	size = 20
	
	## OPTIONAL - DEFINE COLOUR SCHEME
	color_num = Color_db.SMOOTH_RED

	## LOAD EXISTING TILESET:
	spec_num = Spec_db.DEFAULT
	pre_spec = load_spec(spec_num,color_num)
	## OR DEFINE YOUR OWN:
	#A,B,C,D = parse_colors(color_num)
	#pre_spec = [   # COOL STRUCTURES
	#	(C,A,A,C),
	#	(A,D,A,A),
	#	(A,D,A,D),
	#	(A,D,A,D),
	#	(A,D,A,D),
	#	(A,D,A,D),
	#	(B,D,A,D),
	#	(B,D,A,D),
	#	(B,D,B,D),
	#	(B,D,B,D),
	#	(A,D,B,D),
	#	(B,D,A,D),
	#	(A,A,A,D),
	#	(B,D,B,B),
	#	(A,A,B,A),
	#	(B,A,B,A),
	#	(B,A,B,A),
	#	(B,A,B,A),
	#	(B,D,B,A),
	#	(NOP,NOP,NOP,NOP)]


	preset_tiles = []
	preset_tiles.append(0)
else:
#################### TURING MACHINE SPECS ###################

	colour_array = [
		(0,255,0),
		(0,255,255),
		(180,0,180),
		(255,255,0),
		(0,160,255),
		(0,204,204),
		(140,80,255),
		(150,255,120),
		(160,70,0),
		(100,100,100),
		(200,200,0),
		(80,0,80),
		(80,80,0),
		(100,100,20),
		(85,170,20),
		(200,200,120),
		(60,60,170),
		(70,240,160),
		(50,200,120),
		(0,0,0)]


	sides = []
	sides.append("1")
	sides.append("0")
	sides.append("blank")

	#######################################

	states = ["A","B","C","D"]

	x = "blank"			#4-2 Busy Beaver
	pre_spec = [(1,x,1,x),
				(0,x,0,x),
				(x,x,0,x),
				(x,x,"A0",x),
				("A0",x,1,"B"),
				("A1","B",1,x),
				("B0","A",1,x),
				("B1","C",0,x),
				("C0",x,1,x),
				("C1","D",1,x),
				("D0",x,1,"D"),
				("D1",x,0,"A")
				]

	p_UP_BORDER_COLOUR = "blank"
	p_DOWN_BORDER_COLOUR = "blank"	
	rows = 16

	size = 12

	preset_tiles = []
	for i in range(0,rows):
		if i != 4:
			preset_tiles.append(2)
		else:
			preset_tiles.append(3)

	#######################################

	#states = ["A","B","C","D","E"]

	#x = "blank"				#5-2 Busy Beaver (conjectured)
	#pre_spec = [(1,x,1,x),
	#			(0,x,0,x),
	#			(x,x,0,x),
	#			(x,x,"A0",x),
	#			("A0",x,1,"B"),
	#			("A1","C",1,x),
	#			("B0",x,1,"C"),
	#			("B1",x,1,"B"),
	#			("C0",x,1,"D"),
	#			("C1","E",0,x),
	#			("D0","A",1,x),
	#			("D1","D",1,x),
	#			("E0",x,1,x),
	#			("E1","A",0,x)
	#			]

	#p_UP_BORDER_COLOUR = "blank"
	#p_DOWN_BORDER_COLOUR = "blank"	
	#rows = 25
	#size = 10

	#preset_tiles = []
	#for i in range(0,rows):
	#	if i != 9:
	#		preset_tiles.append(2)
	#	else:
	#		preset_tiles.append(3)

	#######################################

	#states = ["A","B"]

	#x = "blank"				#incrementer
	#y = "border"
	#pre_spec = [(1,x,1,x),
	#			(0,x,0,x),
	#			(x,x,0,x),
	#			(x,x,1,x),
	#			(1,x,1,y),
	#			(0,x,0,y),
	#			(x,x,0,y),
	#			(x,x,1,y),
	#			(x,x,"A0",y),
	#			(x,x,"A0",x),
	#			(x,x,"A1",y),
	#			(x,x,"A1",x),
	#			("A0",x,0,"A"),
	#			("A0",x,"B0",y),
	#			("A1",x,1,"A"),
	#			("A1",x,"B1",y),
	#			("B0","A",1,x),
	#			("B1","B",0,x),
	#			("B0","A",1,y),
	#			("B1","B",0,y)
	#			]

	#p_UP_BORDER_COLOUR = "border"
	#p_DOWN_BORDER_COLOUR = "blank"	
	#rows = 17
	#size = 25

	#preset_tiles = []
	#for i in range(0,rows):
	#	if i == 0:
	#		preset_tiles.append(10)
	#	elif i in [1,2,4,5,6,7,8,9,10,11,12,15]:
	#		preset_tiles.append(3)
	#	else:
	#		preset_tiles.append(2)


if STATE_TILES:
	for state in states:
		sides.append(state+"0")
		sides.append(state+"1")
		sides.append(state)

	trans_spec = []
	for state in states:
		trans_spec.append((1,x,state+str(1),state))
		trans_spec.append((0,x,state+str(0),state))
		trans_spec.append((1,state,state+str(1),x))
		trans_spec.append((0,state,state+str(0),x))
		if "y" in vars():
			trans_spec.append((1,state,state+str(1),y))
			trans_spec.append((0,state,state+str(0),y))

	sides_len = len(sides)

	assert (sides_len < len(colour_array))


	sides_dict = {}
	i=0
	for unique_char in sides:
		if unique_char not in [0,1,"blank","border"]:
			sides_dict.update({unique_char:colour_array[i]})
			i+=1

	sides_dict.update({"1":(0,0,255)})
	sides_dict.update({"0":(255,0,0)})
	sides_dict.update({"blank":(180,180,180)})
	sides_dict.update({"border":(40,40,40)})

	spec = []
	class_spec = []

	for row in pre_spec:
		new_row = []
		for element in row:
			new_row.append(sides_dict[str(element)])
		class_spec.append(MySpec(new_row,False))
		spec.append(new_row)

	for row in trans_spec:
		new_row = []
		for element in row:
			new_row.append(sides_dict[str(element)])
		class_spec.append(MySpec(new_row,True))
		spec.append(new_row)

	spec.append((0,0,0,0))
	class_spec.append(MySpec((0,0,0,0),False))
else:
	spec = []
	class_spec = []
	for row in pre_spec:
		class_spec.append(MySpec(row,False))
		spec.append(row)