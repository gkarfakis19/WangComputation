import enum

import colorsys
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
YELLOW = (0,255,255)
MAGENTA = (180,0,180)
CYAN = (255,255,0)
ORANGE = (0,160,255)
DRED = (0,0,160)
BEIGE = (0,204,204)
DGREEN = (40,160,40)
LGREEN = (160,255,40)
PINK = (140,80,255)
LIME = (150,255,120)
LLIME = (170,255,150)
NAVY = (160,70,0)
LNAVY = (180,120,20)
DCYAN = (160,160,0)
GREY = (180,180,180)
DGREY = (110,110,110)
WHITE = (0,0,0)
NOP = (0,0,0)


class Spec_db(enum.Enum):
	STRUCTURES = 1
	WIKIPEDIA = 2
	DEFAULT = 3

class Color_db(enum.Enum):
	# NAMES OF COLOR SCHEMES
	BLUE = 1
	RED = 2
	GREEN = 3
	SMOOTH_RED = 4

# COLOUR SCHEMES:
# THE SPEC CAN DEFINE SPECIFIC COLOURS *OR* GENERIC COLOURS
# IF GENERIC COLOUR IS DEFINED, COLOUR SCHEME CAN BE USED.

def parse_colors(color_scheme):
	if (color_scheme == Color_db.BLUE):
		COL0 = BLUE
		COL1 = NAVY
		COL2 = LNAVY
		COL3 = DCYAN
	elif (color_scheme == Color_db.RED):
		COL0 = RED
		COL1 = DRED
		COL2 = ORANGE
		COL3 = YELLOW
	elif (color_scheme == Color_db.SMOOTH_RED):
		COL0 = hsv2rgb(0.6666,1.0,0.75)
		COL1 = hsv2rgb(0.6666,0.90,0.95)
		COL2 = hsv2rgb(0.6666,0.75,1.0)
		COL3 = hsv2rgb(0.6666,0.6,0.95)
	elif (color_scheme == Color_db.GREEN):
		COL0 = GREEN
		COL1 = DGREEN
		COL2 = LIME
		COL3 = LLIME
	else: #DEFAULT FALLBACK
		COL0 = RED
		COL1 = GREEN
		COL2 = BLUE
		COL3 = ORANGE
	return (COL0,COL1,COL2,COL3)


def load_spec(spec_num,color_scheme = None):
	COL0,COL1,COL2,COL3 = parse_colors(color_scheme)
	pre_spec = (NOP,NOP,NOP,NOP)
	if (spec_num == Spec_db.STRUCTURES):
		pre_spec = [(COL0,COL1,COL0,COL2), # COOL STRUCTURES
			(COL1,COL0,COL2,COL2),
			(COL0,COL2,COL0,COL1),
			(COL1,COL1,COL1,COL0),
			(COL1,COL1,COL0,COL2),
			(COL2,COL0,COL0,COL1),
			(COL0,COL0,COL2,COL0),
			(COL2,COL2,COL1,COL2),
			(COL2,COL0,COL0,COL2),
			(COL1,COL0,COL2,COL1),
			(COL2,COL1,COL1,COL0),
			(NOP,NOP,NOP,NOP)]

	elif (spec_num == Spec_db.WIKIPEDIA):
		pre_spec = [(GREEN,RED,RED,RED), #WIKIPEDIA -- NEEDS VERY ROBUST ERROR HANDLING, NOT SUPPORTED ATM.
			(GREEN,BLUE,RED,BLUE),
			(GREEN,GREEN,GREEN,RED),
			(BLUE,RED,BLUE,ORANGE),
			(BLUE,ORANGE,BLUE,BLUE),
			(ORANGE,RED,ORANGE,ORANGE),
			(ORANGE,BLUE,GREEN,RED),
			(RED,BLUE,ORANGE,BLUE),
			(RED,ORANGE,RED,BLUE),
			(RED,BLUE,GREEN,GREEN),
			(GREEN,RED,ORANGE,RED),
			(NOP,NOP,NOP,NOP)]

	elif (spec_num == Spec_db.DEFAULT or not spec_num):
		pre_spec = [(COL0,COL2,COL0,COL2), #DEFAULT
			(COL2,COL0,COL2,COL0),
			(COL2,COL0,COL0,COL0),
			(COL0,COL0,COL0,COL2),
			(COL2,COL2,COL2,COL0),
			(COL2,COL2,COL0,COL1),
			(COL1,COL0,COL0,COL2),
			(COL0,COL0,COL1,COL0),
			(COL1,COL1,COL2,COL1),
			(COL1,COL0,COL0,COL1),
			(COL2,COL0,COL1,COL2),
			(COL1,COL2,COL2,COL0),
			(NOP,NOP,NOP,NOP)]



	return pre_spec