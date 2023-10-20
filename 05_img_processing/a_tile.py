# 1 ) 바둑판식  타일형을 만들어 보자.

import cv2 as cv
import numpy as np

image = cv.imread('../img/Lenna.png' )

def my_tile(im_list_2d):
    return cv.vconcat([ cv.hconcat( im_list_h)  for  im_list_h  in   im_list_2d   ])

                        #dsize=(h,w)
im01= cv.resize(image,dsize=(0,0),fx=2.0,fy=2.0)  #fx =수평측 비율   fy =수직측 비율

im_tile = my_tile([ [im01,im01,im01,im01],
                    [im01,im01,im01,im01],
                    [im01,im01,im01,im01] ])

cv.imwrite("../img_res05/tile_img03.jpg",im_tile)