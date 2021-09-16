import yaml
import colorsys
#this file accepts an arbitrary turing machine and produces a spec to match

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

class MyState():
	def __init__(self,name,mappings):
		self.mappings = mappings
		self.name = name

tapechars = []
states = []
Border = False
with open("Turing1.yaml", "r") as stream:
	try:
		dict = yaml.safe_load(stream)



		for tapecharacter in dict["tapechars"]:
			if tapecharacter not in [0,1,"border"]:
				print("non-standard char")
			else:
				if tapecharacter == "border":
					Border = True
				else:
					tapechars.append(tapecharacter)

		for top_state_dict in dict["states"]:
			state = list(top_state_dict.values())[0]
			mappings = []
			name = state["name"]
			mapdir = state["maps"]
			mappings.append(mapdir)
			StateClass = MyState(name,mappings)
			states.append(StateClass)
		pass
	except yaml.YAMLError as exc:
		print(exc)
		
sides = []
sides.append("blank")
if Border:
	sides.append("border")
sides.append("error")

pre_spec = []
for tapechar in tapechars:
	sides.append(str(tapechar))
	pre_spec.append((
		str(tapechar),
		"blank",
		str(tapechar),
		"blank"
		))
	if Border:
		pre_spec.append((
			"border",
			"blank",
			str(tapechar),
			"blank"))
		pre_spec.append((
			str(tapechar),
			"blank",
			str(tapechar),
			"border"))
		pre_spec.append((
			str(tapechar),
			"border",
			str(tapechar),
			"blank"))

for state in states:



sides_len = len(sides)
increment = 1.0/sides_len

sides_dict = {}
for i,unique_char in enumerate(sides):
	if unique_char not in ["blank","border"]:
		sides_dict.update({sides[i]:hsv2rgb(i*increment,1.0,1.0)})
	elif unique_char == "blank":
		sides_dict.update({"blank":((150,150,150))})
	elif unique_char == "border":
		sides_dict.update({"border":((80,80,80))})

pre_spec.append(("error","error","error","error"))

spec = []
for row in pre_spec:
	new_row = []
	for element in row:
		new_row.append(sides_dict[element])
	spec.append(new_row)
pass
