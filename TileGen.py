import cv2 as cv
import numpy as np
from TuringSpec import *

Manual = True
if Manual:
    W = 50
    H = 50

    RED = (0,0,255)
    GREEN = (0,255,0)
    BLUE = (255,0,0)
    YELLOW = (0,255,255)
    MAGENTA = (180,0,180)
    CYAN = (255,255,0)
    ORANGE = (0,160,255)
    BEIGE = (0,204,204)
    PINK = (140,80,255)
    LIME = (150,255,120)
    NAVY = (160,70,0)
    GREY = (180,180,180)
    DGREY = (110,110,110)
    NOP = (0)
    WHITE = NOP

    path = 'C:/Users/georg/source/repos/WangComputation/Images/'

    def my_line(img, start, end,thick=1):
        thickness = thick
        line_type = 8
        cv.line(img,
                 start,
                 end,
                 (255,128,128),
                 thickness,
                 line_type)


    def triangle_fill(image,pos,colour):
        if (pos == 1):
            triangle = np.array([[0,0],[0,H],[W/2,H/2]])
        elif (pos == 2):
            triangle = np.array([[0,H],[W,H],[W/2,H/2]])
        elif (pos == 3):
            triangle = np.array([[W,H],[W,0],[W/2,H/2]])
        elif (pos == 4):
            triangle = np.array([[W,0],[0,0],[W/2,H/2]])
        cv.fillPoly(image,np.int32([triangle]),color=colour)

    def TileGen(spec):
        image_arr = []
        for row in spec:
            image = np.zeros((W,H,3),dtype=np.uint8)
            image[:][:][:] = 255;

            index = 0
            for column in row:
                index+=1
                if column!=0:
                    triangle_fill(image,index,column)
            my_line(image,(0,0),(W,H))
            my_line(image,(0,H),(W,0))

            my_line(image,(0,0),(0,H))
            my_line(image,(0,H),(W,H))
            my_line(image,(W,H),(W,0))
            my_line(image,(W,0),(0,0))
            image_arr.append(image)

        return image_arr;

    #spec = [(GREEN,RED,RED,RED), #WIKIPEDIA
    #        (GREEN,BLUE,RED,BLUE),
    #        (GREEN,GREEN,GREEN,RED),
    #        (BLUE,RED,BLUE,ORANGE),
    #        (BLUE,ORANGE,BLUE,BLUE),
    #        (ORANGE,RED,ORANGE,ORANGE),
    #        (ORANGE,BLUE,GREEN,RED),
    #        (RED,BLUE,ORANGE,BLUE),
    #        (RED,ORANGE,RED,BLUE),
    #        (RED,BLUE,GREEN,GREEN),
    #        (GREEN,RED,ORANGE,RED),
    #        (NOP,NOP,NOP,NOP)]

    #spec = [(BLUE,LIME,BLUE,LIME), #WORKS
    #        (LIME,BLUE,LIME,BLUE),
    #        (LIME,BLUE,BLUE,BLUE),
    #        (BLUE,BLUE,BLUE,LIME),
    #        (LIME,LIME,LIME,BLUE),
    #        (LIME,LIME,BLUE,CYAN),
    #        (CYAN,BLUE,BLUE,LIME),
    #        (BLUE,BLUE,CYAN,BLUE),
    #        (CYAN,CYAN,LIME,CYAN),
    #        (CYAN,BLUE,BLUE,CYAN),
    #        (LIME,BLUE,CYAN,LIME),
    #        (CYAN,LIME,LIME,BLUE),
    #        (NOP,NOP,NOP,NOP)]

    #spec = [(NOP,NOP,NOP,NOP), #ADDITION
    #        (GREY,NOP,NOP,NOP),
    #        (NOP,NOP,NOP,GREY),
    #        (GREY,RED,NOP,GREY),
    #        (GREY,CYAN,NOP,RED),
    #        (GREY,NOP,YELLOW,CYAN),
    #        (YELLOW,CYAN,NOP,NOP),
    #        (NOP,NOP,YELLOW,CYAN),
    #        (YELLOW,NOP,ORANGE,GREEN),
    #        (NOP,GREEN,NOP,GREEN),
    #        (NOP,GREEN,NOP,GREY),
    #        (ORANGE,NOP,ORANGE,NOP),
    #        (ORANGE,NOP,BLUE,GREEN),
    #        (BLUE,NOP,NOP,MAGENTA),
    #        (NOP,MAGENTA,BLUE,NOP),
    #        (NOP,MAGENTA,NOP,GREY),
    #        (BLUE,BLUE,BLUE,BLUE)]

    #spec = [(NOP,NOP,NOP,NOP), #FIB
    #        (GREY,NOP,NOP,NOP),
    #        (NOP,NOP,NOP,GREY),
    #        (GREY,YELLOW,GREEN,GREY),
    #        (GREEN,RED,CYAN,GREY),
    #        (CYAN,BLUE,CYAN,GREY),
    #        (CYAN,NOP,CYAN,GREY),
    #        (GREY,BEIGE,ORANGE,YELLOW),
    #        (MAGENTA,RED,LIME,RED),
    #        (LIME,RED,NOP,BLUE),
    #        (LIME,NOP,NOP,GREEN),
    #        (NOP,GREEN,LIME,NOP),
    #        (GREY,NOP,PINK,BEIGE),
    #        (PINK,BEIGE,NOP,NOP),
    #        (PINK,BEIGE,MAGENTA,RED),
    #        (MAGENTA,NOP,MAGENTA,NOP),
    #        (ORANGE,RED,LIME,RED),
    #        (NOP,NOP,PINK,BEIGE),
    #        (NOP,RED,NOP,RED),
    #        (BLUE,BLUE,BLUE,BLUE)]

    #spec = [(DGREY,GREY,RED,DGREY), #n-bit turing counter
    #        (RED,MAGENTA,ORANGE,DGREY),
    #        (ORANGE,GREY,PINK,DGREY),
    #        (PINK,GREY,CYAN,DGREY),
    #        (DGREY,DGREY,NAVY,GREY),
    #        (NAVY,DGREY,BLUE,MAGENTA),
    #        (BLUE,DGREY,BLUE,GREY),
    #        (DGREY,DGREY,ORANGE,GREY),
    #        (ORANGE,DGREY,NAVY,GREY),
    #        (RED,GREY,RED,DGREY),
    #        (DGREY,GREY,ORANGE,DGREY), #start1,10
    #        (RED,GREY,RED,DGREY),
    #        (BLUE,MAGENTA,NAVY,DGREY),
    #        (NAVY,GREY,CYAN,DGREY),
    #        (CYAN,BEIGE,RED,DGREY),
    #        (DGREY,DGREY,RED,GREY), #start2,15
    #        (RED,DGREY,RED,GREY),
    #        (ORANGE,DGREY,RED,MAGENTA),
    #        (RED,DGREY,PINK,BEIGE),
    #        (PINK,DGREY,BLUE,MAGENTA),
    #        (DGREY,GREY,BLUE,GREY),#start3,20
    #        (DGREY,GREY,RED,GREY), #start4,21
    #        (RED,GREY,RED,GREY),
    #        (BLUE,GREY,BLUE,GREY), 
    #        (RED,GREY,PINK,BEIGE), 
    #        (BLUE,GREY,CYAN,BEIGE), 
    #        (RED,MAGENTA,ORANGE,GREY), 
    #        (BLUE,MAGENTA,NAVY,GREY), 
    #        (ORANGE,GREY,RED,MAGENTA), 
    #        (NAVY,GREY,BLUE,MAGENTA), 
    #        (CYAN,BEIGE,RED,GREY), 
    #        (PINK,GREY,BLUE,MAGENTA), 
    #        (BLUE,DGREY,CYAN,BEIGE), 
    #        (CYAN,DGREY,WHITE,GREY), 
    #        (PINK,PINK,PINK,PINK)]

    if  __name__=='__main__':
        image_arr = TileGen(spec)
        index=0
        f = open("image_specs.txt", "w")
        for im in image_arr:
            cv.imshow("Tile",im)
            cv.waitKey(0)
            cv.imwrite(path+"image"+str(index)+".jpg",im)
            f.write(str(spec[index]))
            f.write("\n")
            index+=1
        f.close()

        cv.destroyAllWindows()
    else:
        image_arr = TileGen(spec)
        index=0
        f = open("image_specs.txt", "w")
        for im in image_arr:
            cv.imwrite(path+"image"+str(index)+".jpg",im)
            f.write(str(spec[index]))
            f.write("\n")
            index+=1
        f.close()