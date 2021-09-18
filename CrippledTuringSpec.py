import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

class MySpec(object):
	def __init__(self,colour,istrans):
		self.colour=colour
		self.istrans=istrans

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

#states = ["A","B","C","D"]

#x = "blank"			#4-2 Busy Beaver
#pre_spec = [(1,x,1,x),
#			(0,x,0,x),
#			(x,x,0,x),
#			(x,x,"A0",x),
#			("A0",x,1,"B"),
#			("A1","B",1,x),
#			("B0","A",1,x),
#			("B1","C",0,x),
#			("C0",x,1,x),
#			("C1","D",1,x),
#			("D0",x,1,"D"),
#			("D1",x,0,"A")
#			]

states = ["A","B","C","D","E"]

x = "blank"				#5-2 Busy Beaver (conjectured)
pre_spec = [(1,x,1,x),
			(0,x,0,x),
			(x,x,0,x),
			(x,x,"A0",x),
			("A0",x,1,"B"),
			("A1","C",1,x),
			("B0",x,1,"C"),
			("B1",x,1,"B"),
			("C0",x,1,"D"),
			("C1","E",0,x),
			("D0","A",1,x),
			("D1","D",1,x),
			("E0",x,1,x),
			("E1","A",0,x)
			]

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

sides_len = len(sides)

assert (sides_len < len(colour_array))


sides_dict = {}
i=0
for unique_char in sides:
	if unique_char not in [0,1,"blank"]:
		sides_dict.update({unique_char:colour_array[i]})
		i+=1

sides_dict.update({"1":(0,0,255)})
sides_dict.update({"0":(255,0,0)})
sides_dict.update({"blank":(180,180,180)})

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