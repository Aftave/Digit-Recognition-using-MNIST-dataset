import pygame, sys
from tokenize import Number
from numpy import testing
from numpy.lib.type_check import imag
from pygame import image
from pygame.locals import *
import numpy as np 
from keras.models import load_model
import cv2
import os
from tensorflow.python.keras.backend import constant
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

boundary_inc = 5

WINDOWSIZEX = 640
WINDOWSIZEY = 480

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

IMAGESAVE = False
MODEL = load_model("model.keras")

LABELS = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR",5:"FIVE", 6:"SIX",
         7:"SEVEN", 8:"EIGHT", 9:"NINE"}

pygame.init()

FONT = pygame.font.Font("FreeSansBold.ttf",18)
DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
WHILE_INIT = DISPLAYSURF.map_rgb(WHITE)
pygame.display.set_caption("DIGIT BOARD")

image_count = 1
Predict = True

iswriting = False

number_xcord = []
number_ycord = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord),4,0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)


        if event.type == MOUSEBUTTONDOWN:
            iswriting = True

        if event.type == MOUSEBUTTONUP:
            iswriting = False
            number_xcord = sorted(number_xcord)
            number_ycord = sorted(number_ycord)

            rect_min_x , rect_max_x = max(number_xcord[0]-boundary_inc, 0), min(WINDOWSIZEX,number_xcord[-1]+boundary_inc)
            rect_min_y , rect_max_y = max(number_ycord[0]-boundary_inc, 0), min(number_ycord[-1]+boundary_inc,WINDOWSIZEX)

            number_xcord = []
            number_ycord = []
            
            img_arr = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x:rect_max_x, rect_min_y:rect_max_y].T.astype(np.float32)

            if IMAGESAVE:
                cv2.imwrite("image.png")
                image_count+=1

            if Predict:
                image = cv2.resize(img_arr, (28,28))
                image = np.pad(image,(10,10), 'constant', constant_values=0)
                image = cv2.resize(image,(28,28))/255


                label = str(LABELS[np.argmax(MODEL.predict(image.reshape(1,28,28,1)))])

                surface = pygame.Surface((10,5))

                text_surf = FONT.render(label, True, RED, WHITE)
                text_rect = surface.get_rect(topleft=(10,20))
                # textRecObj = testing.get_rect()
                # textRecObj.left, textRecObj.bottom = rect_min_x, rect_max_y

                DISPLAYSURF.blit(text_surf,text_rect)

            if event.type == KEYDOWN:
                if event.unicode == "n":
                    DISPLAYSURF.fill(BLACK)

    pygame.display.update()


