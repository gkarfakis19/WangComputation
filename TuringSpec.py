#import yaml
#import colorsys
##this file accepts an arbitrary turing machine and produces a spec to match


## DEPRECATED


#def hsv2rgb(h,s,v):
#    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

#class MyState():
#	def __init__(self,name,mappings):
#		self.mappings = mappings
#		self.name = name

#tapechars = []
#states = []
#Border = False
#with open("Turing1.yaml", "r") as stream:
#	try:
#		dict = yaml.safe_load(stream)



#		for tapecharacter in dict["tapechars"]:
#			if tapecharacter not in [0,1,"border"]:
#				print("non-standard char")
#			else:
#				if tapecharacter == "border":
#					Border = True
#				else:
#					tapechars.append(tapecharacter)

#		for top_state_dict in dict["states"]:
#			state = list(top_state_dict.values())[0]
#			mappings = []
#			name = state["name"]
#			mapdir = state["maps"]
#			mappings.append(mapdir)
#			StateClass = MyState(name,mappings)
#			states.append(StateClass)
#		pass
#	except yaml.YAMLError as exc:
#		print(exc)
		
#sides = []
#sides.append("blank")
#if Border:
#	sides.append("border")
#sides.append("error")

#pre_spec = []
#for tapechar in tapechars:
#	sides.append(str(tapechar))
#	pre_spec.append((
#		str(tapechar),
#		"blank",
#		str(tapechar),
#		"blank"
#		))
#	if Border:
#		pre_spec.append((
#			"border",
#			"blank",
#			str(tapechar),
#			"blank"))
#		pre_spec.append((
#			str(tapechar),
#			"blank",
#			str(tapechar),
#			"border"))
#		pre_spec.append((
#			str(tapechar),
#			"border",
#			str(tapechar),
#			"blank"))

#for state in states:
#	sides.append(str(state.name)) #head/state transition
#	for tapechar in tapechars:
#		if tapechar != "border":
#			sides.append(str(state.name)+str(tapechar)) #state action
#	for mapping in state.mappings[0]:
#		map_info = list(mapping.values())[0]
#		curr_tapechar = str(list(mapping.keys())[0])
#		if curr_tapechar == "border":
#			for tapechar in tapechars:
#				pre_spec.append((str(state.name)+str(tapechar),"blank",str(map_info["next"])+str(tapechar),"border"))
#				pre_spec.append((str(state.name)+str(tapechar),"border",str(map_info["next"])+str(tapechar),"blank"))
#			continue
#		new_tile = []
#		new_tile.append(str(state.name)+curr_tapechar)
#		if Border:
#			new_border_tile = new_tile.copy()
#		if map_info["dir"] == "R": #R means UP
#			new_tile.append("blank")
#			new_tile.append(map_info["to"])
#			new_tile.append(map_info["next"])
#			if Border:
#				new_border_tile.append("border")
#				new_border_tile.append(str(map_info["to"]))
#				new_border_tile.append(map_info["next"])
#		elif map_info["dir"] == "L": #L means DOWN
#			new_tile.append(map_info["next"])
#			new_tile.append(map_info["to"])
#			new_tile.append("blank")
#			if Border:
#				new_border_tile.append(map_info["next"])
#				new_border_tile.append(str(map_info["to"]))
#				new_border_tile.append("border")
#		pre_spec.append(tuple(new_tile))
#		if Border:
#			pre_spec.append(tuple(new_border_tile))
#		if Border:
#			pre_spec.append(("border","border","","blank"))



#sides_len = len(sides)
#increment = 1.0/sides_len

#sides_dict = {}
#for i,unique_char in enumerate(sides):
#	if unique_char not in ["blank","border"]:
#		sides_dict.update({sides[i]:hsv2rgb(i*increment,1.0,1.0)})
#	elif unique_char == "blank":
#		sides_dict.update({"blank":((150,150,150))})
#	elif unique_char == "border":
#		sides_dict.update({"border":((80,80,80))})

#sides_dict["0"]=(0,0,0)
#sides_dict["1"]=(255,255,255)

#pre_spec.append(("error","error","error","error"))

#spec = []
#for row in pre_spec:
#	new_row = []
#	for element in row:
#		new_row.append(sides_dict[str(element)])
#	spec.append(new_row)
#pass
