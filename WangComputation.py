##!/usr/bin/env python

import pygame
import sys, os
from pygame.locals import *
from TileClass import *
import random
import pprint
import enum

TILE_NUM = len(spec)-1
DISP = (1500,800)

class Modes(enum.Enum):
    ADDITION_M = 1
    FIB_M = 2
    TURING_M = 3

class Colours(enum.Enum):
    WHITE_C = 0
    RED_C = 1
    GREEN_C = 2
    BLUE_C = 3
    YELLOW_C = 4
    MAGENTA_C = 5
    CYAN_C = 6
    ORANGE_C = 7
    BEIGE_C = 8
    PINK_C = 9
    LIME_C = 10
    NAVY_C = 11
    GREY_C = 12
    DGREY_C = 13

def LoadTable(max_tile_num):
    tiletable = []
    for i in range(max_tile_num):
        img = pygame.image.load("Images/image"+str(i)+".jpg").convert()
        tile = TileClass(parsed_spec[i][0],parsed_spec[i][1],parsed_spec[i][2],parsed_spec[i][3],img)
        tiletable.append(tile)
    err_tile = TileClass(0,0,0,0,pygame.image.load("Images/image"+str(TILE_NUM)+".jpg").convert())
    return err_tile,tiletable

def PlaceTile(tile_num,pos,matrix):
    arg1=int(pos[1]/H)
    arg2=int(pos[0]/W)
    tile_n = parsed_spec[tile_num]
    matrix[arg1][arg2][:] = tile_n
    screen.blit(table[tile_num].img,pos)

def PlaceErrTile(pos,matrix):
    matrix[int(pos[1]/H)][int(pos[0]/W)][:] = [0,0,0,0]
    screen.blit(err_tile.img,pos)

def SearchTableWOne(table,des_colour,pos):
    findings = []
    for i,tile in enumerate(table):
        if tile.colours[pos] == des_colour:
            findings.append(i)
    if len(findings) is not 0:
        rand = random.randint(0,len(findings))
        return findings[rand-1]
    return None

def SearchTableWTwo(table,des_colour0,pos0,des_colour1,pos1,restricted_colour = None):
    if restricted_colour is None:
        if des_colour1 == None:
            return SearchTableWOne(table,des_colour0,pos0)
        elif des_colour0 == None:
            return SearchTableWOne(table,des_colour1,pos1)
        else:
            findings = []
            for i,tile in enumerate(table):
                if tile.colours[pos0] == des_colour0 and tile.colours[pos1] == des_colour1:
                    findings.append(i)
            if len(findings) is not 0:
                rand = random.randint(0,len(findings))
                return findings[rand-1]
            return None
    else:
        if des_colour1 == None:
            return SearchTableWOne(table,des_colour0,pos0)
        elif des_colour0 == None:
            return SearchTableWOne(table,des_colour1,pos1)
        else:
            findings = []
            for i,tile in enumerate(table):
                if tile.colours[pos0] == des_colour0 and tile.colours[pos1] == des_colour1:
                    if restricted_colour not in tile.colours[:]:
                        findings.append(i)
            if len(findings) is not 0:
                rand = random.randint(0,len(findings))
                return findings[rand-1]
            return None

def SearchTableWThree(table,des_colour0,pos0,des_colour1,pos1,des_colour2,pos2):
    findings = []
    for i,tile in enumerate(table):
        if tile.colours[pos0] == des_colour0 and tile.colours[pos1] == des_colour1 and tile.colours[pos2] == des_colour2:
            findings.append(i)
    if len(findings) is not 0:
        rand = random.randint(0,len(findings))
        return findings[rand-1]
    return None

parsed_spec =[]
for i,tile in enumerate(spec):
    parsed_spec.append([])
    for colour in tile:
            if colour == RED:
                parsed_spec[i].append(Colours.RED_C)
            elif colour == BLUE:
                parsed_spec[i].append(Colours.BLUE_C)
            elif colour == GREEN:
                parsed_spec[i].append(Colours.GREEN_C)
            elif colour == YELLOW:
                parsed_spec[i].append(Colours.YELLOW_C)
            elif colour == MAGENTA:
                parsed_spec[i].append(Colours.MAGENTA_C)
            elif colour == CYAN:
                parsed_spec[i].append(Colours.CYAN_C)
            elif colour == ORANGE:
                parsed_spec[i].append(Colours.ORANGE_C)
            elif colour == BEIGE:
                parsed_spec[i].append(Colours.BEIGE_C)
            elif colour == PINK:
                parsed_spec[i].append(Colours.PINK_C)
            elif colour == LIME:
                parsed_spec[i].append(Colours.LIME_C)
            elif colour == NAVY:
                parsed_spec[i].append(Colours.NAVY_C)
            elif colour == GREY:
                parsed_spec[i].append(Colours.GREY_C)
            elif colour == DGREY:
                parsed_spec[i].append(Colours.DGREY_C)
            elif colour == NOP:
                parsed_spec[i].append(Colours.WHITE_C)
        

Mode = Modes.TURING_M
#ADD1 = 5
#ADD2 = 7

if __name__=='__main__' and Mode == Modes.ADDITION_M:

    preset_table = []
    for i in range(0,25):
        preset_table.append((i,0))

    preset_tiles = []
    for i in range(0,25):
        if i == 0:
            num = 3
        elif i == ADD1-1 or i == ADD2-1:
            num = 10
        else:
            num = 2
        preset_tiles.append(num)


    UP_BORDER_COLOUR = Colours.GREY_C
    LEFT_BORDER_COLOUR = Colours.GREY_C
    DOWN_BORDER_COLOUR = Colours.WHITE_C

    pygame.init()
    screen = pygame.display.set_mode(DISP)
    screen.fill((255, 255, 255))
    rows = int(DISP[1]/H)
    cols = int(DISP[0]/W)

    matrix = [[[0 for k in range(4)] for j in range(cols)] for i in range(rows)]

    err_tile,table = LoadTable(TILE_NUM)
    i=0
    j=0
    Err_Flag = False
    while 1:
        Preset_Found = False
        if (j<cols):
            if(i<rows):
                for k in range(0,len(preset_table)):
                    if preset_table[k]==(j,i):
                        PlaceTile(preset_tiles[k],(j*W,i*H),matrix)
                        preset_table.pop(k)
                        preset_tiles.pop(k)
                        i+=1
                        Preset_Found = True
                        break
                if (Preset_Found):
                    continue
                else:
                    if i==0: # first horiz
                        des_colour = matrix[0][j-1][2]
                        res = SearchTableWTwo(table,des_colour,0, UP_BORDER_COLOUR, 3)
                        if res is not None:
                            PlaceTile(res,(j*W,i*H),matrix)
                        else:
                            PlaceErrTile((j*W,i*H),matrix)
                        i+=1
                    else:
                        if j==0: # first vert
                            des_colour = matrix[i-1][j][1]
                            res = SearchTableWTwo(table,des_colour,3,LEFT_BORDER_COLOUR, 0)
                            if res is not None:
                                PlaceTile(res,(j*W,i*H),matrix)
                            else:
                                PlaceErrTile((j*W,i*H),matrix)
                            i+=1
                        else: #normal case
                            des_colour0 = matrix[i-1][j][1]
                            des_colour1 = matrix[i][j-1][2]
                            res = SearchTableWTwo(table,des_colour0,3,des_colour1,0)
                            if (des_colour0==Colours.WHITE_C) and (des_colour1==Colours.WHITE_C) and not Err_Flag:
                                PlaceTile(0,(j*W,i*H),matrix)
                                i+=1
                            else:
                                if res is not None:
                                    PlaceTile(res,(j*W,i*H),matrix)
                                    i+=1
                                else:
                                    PlaceErrTile((j*W,i*H),matrix)
                                    Err_Flag = True
                                    i-=1
                                    continue
                    if (Err_Flag):
                        Err_Flag = False
            else:
                i=0
                j+=1


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit(0)
   
        pygame.display.update() 
        pygame.time.delay(5)

if __name__=='__main__' and Mode == Modes.FIB_M:

    preset_table = []
    preset_table.append((0,0))
    for i in range(0,1000):
        preset_table.append((i,0))

    preset_tiles = []
    preset_tiles.append(3)
    for i in range(0,1000):
        if i == 0:
            num = 3
        elif i == 1:
            num = 4
        else:
            num = 2
        preset_tiles.append(num)


    UP_BORDER_COLOUR = Colours.GREY_C
    LEFT_BORDER_COLOUR = Colours.GREY_C
    DOWN_BORDER_COLOUR = Colours.WHITE_C

    #preset_table = []
    #preset_table.append((0,0))

    #preset_tiles = []
    #preset_tiles.append(0)

   
    #UP_BORDER_COLOUR = None
    #LEFT_BORDER_COLOUR = None

    pygame.init()
    screen = pygame.display.set_mode(DISP)
    screen.fill((255, 255, 255))
    rows = int(DISP[1]/H)
    cols = int(DISP[0]/W)

    matrix = [[[0 for k in range(4)] for j in range(cols)] for i in range(rows)]

    err_tile,table = LoadTable(TILE_NUM)
    i=0
    j=0
    Err_Flag = False
    while 1:
        Preset_Found = False
        if (j<cols):
            if(i<rows):
                for k in range(0,len(preset_table)):
                    if preset_table[k]==(j,i):
                        PlaceTile(preset_tiles[k],(j*W,i*H),matrix)
                        preset_table.pop(k)
                        preset_tiles.pop(k)
                        i+=1
                        Preset_Found = True
                        break
                if (Preset_Found):
                    continue
                else:
                    if i==0: # first horiz
                        des_colour = matrix[0][j-1][2]
                        if des_colour == Colours.WHITE_C:
                            res = SearchTableWOne(table,UP_BORDER_COLOUR,3)
                        else:
                            res = SearchTableWTwo(table,des_colour,0, UP_BORDER_COLOUR, 3)
                        if res is not None:
                            PlaceTile(res,(j*W,i*H),matrix)
                        else:
                            PlaceErrTile((j*W,i*H),matrix)
                        i+=1
                    else:
                        if j==0: # first vert
                            des_colour = matrix[i-1][j][1]
                            res = SearchTableWTwo(table,des_colour,3,LEFT_BORDER_COLOUR, 0)
                            if res is not None:
                                PlaceTile(res,(j*W,i*H),matrix)
                            else:
                                PlaceErrTile((j*W,i*H),matrix)
                            i+=1
                        else: #normal case
                            des_colour0 = matrix[i-1][j][1]
                            des_colour1 = matrix[i][j-1][2]
                            res = SearchTableWTwo(table,des_colour0,3,des_colour1,0)
                            if (des_colour0==Colours.WHITE_C) and (des_colour1==Colours.WHITE_C) and not Err_Flag:
                                PlaceTile(0,(j*W,i*H),matrix)
                                i+=1
                            else:
                                if res is not None:
                                    PlaceTile(res,(j*W,i*H),matrix)
                                    i+=1
                                else:
                                    PlaceErrTile((j*W,i*H),matrix)
                                    Err_Flag = True
                                    i-=1
                                    continue
                    if Err_Flag:
                        Err_Flag = False
            else:
                i=0
                j+=1


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit(0)
   
        pygame.display.update() 

if __name__=='__main__' and Mode == Modes.TURING_M:


    UP_BORDER_COLOUR = Colours.DGREY_C
    LEFT_BORDER_COLOUR = Colours.GREY_C
    DOWN_BORDER_COLOUR = Colours.DGREY_C

    pygame.init()
    screen = pygame.display.set_mode(DISP)
    screen.fill((255, 255, 255))
    rows = 17
    cols = int(DISP[0]/W)


    preset_table = []
    for i in range(0,rows):
        preset_table.append((0,i))

    preset_tiles = []
    preset_tiles.append(10)
    preset_tiles.append(21)
    preset_tiles.append(21)
    preset_tiles.append(21)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(20)
    preset_tiles.append(21)
    preset_tiles.append(15)

    matrix = [[[0 for k in range(4)] for j in range(cols)] for i in range(rows)]

    err_tile,table = LoadTable(TILE_NUM)
    i=0
    j=0
    while 1:
        if i<0:
            i=0
        if j<0:
            j=0
        Preset_Found = False
        if (j<cols):
            if(i<rows):
                for k in range(0,len(preset_table)):
                    if preset_table[k]==(j,i):
                        PlaceTile(preset_tiles[k],(j*W,i*H),matrix)
                        preset_table.pop(k)
                        preset_tiles.pop(k)
                        i+=1
                        Preset_Found = True
                        break
                if (Preset_Found):
                    continue
                else:
                    if i==0: # first horiz
                        des_colour = matrix[0][j-1][2]
                        res = SearchTableWTwo(table,des_colour,0, UP_BORDER_COLOUR, 3)
                        if res is not None:
                            PlaceTile(res,(j*W,i*H),matrix)
                            i+=1
                        else:
                            PlaceErrTile((j*W,i*H),matrix)
                            continue
                    elif i==rows-1: # last horiz
                        des_colour0 = matrix[i-1][j][1]
                        des_colour1 = matrix[i][j-1][2]
                        des_colour2 = DOWN_BORDER_COLOUR
                        res = SearchTableWThree(table,des_colour0,3,des_colour1,0,des_colour2,1)
                        if res is not None:
                            PlaceTile(res,(j*W,i*H),matrix)
                            i+=1
                        else:
                            PlaceErrTile((j*W,i*H),matrix)
                            i-=1
                            continue
                    else:
                        if j==0: # first vert
                            des_colour = matrix[i-1][j][1]
                            res = SearchTableWTwo(table,des_colour,3,LEFT_BORDER_COLOUR, 0)
                            if res is not None:
                                PlaceTile(res,(j*W,i*H),matrix)
                            else:
                                PlaceErrTile((j*W,i*H),matrix)
                            i+=1
                        else: #normal case
                            des_colour0 = matrix[i-1][j][1]
                            des_colour1 = matrix[i][j-1][2]
                            if des_colour0 is Colours.DGREY_C:
                                des_colour0 = Colours.GREY_C
                            res = SearchTableWTwo(table,des_colour0,3,des_colour1,0,restricted_colour = Colours.DGREY_C)
                            if res is not None:
                                PlaceTile(res,(j*W,i*H),matrix)
                                i+=1
                            else:
                                PlaceErrTile((j*W,i*H),matrix)
                                i-=1
                                continue
            else:
                Err_backlog = 0
                i=0
                j+=1


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.display.quit()
                sys.exit(0)
   
        pygame.display.update() 
