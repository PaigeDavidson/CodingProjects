#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s24_hw06_uts.py
# description: unit tests for CS 3430: S24: Assignment 06
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
import math
from PIL import Image
import numpy as np
from cs3430_s24_hw06 import *

class cs3430_s24_hw06_uts(unittest.TestCase):

    @staticmethod
    def __test_dex_pil_img(imgpath, outpath):
        input_image  = Image.open(imgpath)
        output_image = dex_pil(input_image, default_delta=1.0, magn_thresh=20)
        output_image.save(outpath)
        del input_image
        del output_image

    ### ================== Unit Tests for Problem 1 =========================        

    def test_problem_01_ut01(self):
        img1 = Image.open('imgs/EdgeImage_01.jpg')
        assert img1.getpixel((1,151)) == (255, 255, 255)
        assert img1.getpixel((1,152)) ==  (0, 0, 0)
        assert img1.getpixel((1,153)) ==  (0, 0, 0)
        dx, dy = pil_pix_dxdy(img1, (1,152), 1)
        assert dx == 1
        assert np.allclose(dy, 255)

    def test_problem_01_ut02(self):
        img1 = Image.open('imgs/EdgeImage_01.jpg')
        assert img1.getpixel((1,150)) ==  (255, 255, 255)
        assert img1.getpixel((1,149)) ==  (255, 255, 255)
        assert pil_pix_dxdy(img1, (1,149), 1) == (1, 1)
        dx, dy = pil_pix_dxdy(img1, (1,149), 1.e-6)
        assert np.allclose(dx, 1.e-6) and np.allclose(dy, 1.e-6)

    def test_problem_01_ut03(self):
        img1 = Image.open('imgs/EdgeImage_01.jpg')
        assert img1.getpixel((1,150)) ==  (255, 255, 255)
        assert img1.getpixel((1,149)) ==  (255, 255, 255)
        assert pil_pix_dxdy(img1, (1,149), 1) == (1, 1)
        dx, dy = pil_pix_dxdy(img1, (1,149), 1.e-6)
        assert np.allclose(dx, 1.e-6) and np.allclose(dy, 1.e-6)
    
    def test_problem_01_ut04(self):
        img1 = Image.open('imgs/EdgeImage_01.jpg')
        assert img1.getpixel((1,151)) == (255, 255, 255)
        assert img1.getpixel((1,152)) ==  (0, 0, 0)
        assert img1.getpixel((1,153)) ==  (0, 0, 0)
        dx, dy = pil_pix_dxdy(img1, (1,152), 1)
        gm = grd_magn(dx,dy)
        np.allclose(gm, 255)
        dt = grd_deg_theta(dx,dy)
        np.allclose(dt, 90)

    def test_problem_01_ut05(self):
        img7 = Image.open('imgs/EdgeImage_07.jpg')
        assert img7.getpixel((1,100)) == (255, 255, 255)
        assert img7.getpixel((1,101)) == (0, 0, 0)
        assert img7.getpixel((1,102)) == (3, 3, 3)
        dx,dy = pil_pix_dxdy(img7, (1,101), 1)
        assert np.allclose(dx, 1)
        assert np.allclose(dy, 252)

    def test_problem_01_ut06(self):
        img7 = Image.open('imgs/EdgeImage_07.jpg')
        assert img7.getpixel((1,100)) == (255, 255, 255)
        assert img7.getpixel((1,101)) == (0, 0, 0)
        assert img7.getpixel((1,102)) == (3, 3, 3)
        dx,dy = pil_pix_dxdy(img7, (1,101), 1)
        assert np.allclose(dx, 1)
        assert np.allclose(dy, 252)
        gm = grd_magn(dx,dy)
        assert np.allclose(gm, 252)
        dt = grd_deg_theta(dx,dy)
        assert np.allclose(dt, 90)

    def test_problem_01_ut07(self):
        img7 = Image.open('imgs/EdgeImage_07.jpg')
        assert img7.getpixel((1,200)) == (0, 0, 0)
        assert img7.getpixel((1,201)) == (255, 255, 255)
        assert img7.getpixel((1,202)) == (253, 253, 253)
        dx,dy = pil_pix_dxdy(img7, (1,201), 1)
        assert np.allclose(dx, 1)
        assert np.allclose(dy, -253)
        gm = grd_magn(dx,dy)
        assert np.allclose(gm, 253)
        dt = grd_deg_theta(dx,dy)
        assert np.allclose(dt, -90)

    def test_problem_01_ut08(self):
        img6 = Image.open('imgs/EdgeImage_06.jpg')
        assert img6.getpixel((199,1)) == (255, 255, 255)
        assert img6.getpixel((200,1)) == (254, 254, 254)
        assert img6.getpixel((201,1)) == (3, 3, 3)
        dx,dy = pil_pix_dxdy(img6, (200,1), 1)
        np.allclose(dx, -252)
        np.allclose(dy, 1)
        gm = grd_magn(dx,dy)
        assert np.allclose(gm, 252)
        dt = grd_deg_theta(dx,dy)
        assert np.allclose(dt,180)

    def test_problem_01_ut09(self):
        img6 = Image.open('imgs/EdgeImage_06.jpg')
        assert img6.getpixel((100,1)) == (4, 4, 4)
        assert img6.getpixel((101,1)) == (252, 252, 252)
        assert img6.getpixel((102,1)) == (255, 255, 255)
        dx,dy = pil_pix_dxdy(img6, (101,1), 1)
        assert np.allclose(dx,251)
        assert np.allclose(dy,1)
        gm = grd_magn(dx,dy)
        assert np.allclose(gm, 251)
        dt = grd_deg_theta(dx,dy)
        assert np.allclose(dt,1)
        
    ### ================== Unit Tests for Problem 2 =========================

    def test_dex_pil_ut01(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/EdgeImage_01.jpg',
                                               'out_imgs/Edge_image_01_dex.jpg')

    def test_dex_pil_ut02(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/EdgeImage_02.jpg',
                                               'out_imgs/Edge_image_02_dex.jpg')

    def test_dex_pil_ut03(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/EdgeImage_03.jpg',
                                               'out_imgs/Edge_image_03_dex.jpg')

    def test_dex_pil_ut04(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/EdgeImage_04.jpg',
                                               'out_imgs/Edge_image_04_dex.jpg')
    
    def test_dex_pil_ut05(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/EdgeImage_05.jpg',
                                               'out_imgs/Edge_image_05_dex.jpg')

    def test_dex_pil_ut06(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/EdgeImage_06.jpg',
                                               'out_imgs/Edge_image_06_dex.jpg')

    def test_dex_pil_ut07(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/EdgeImage_07.jpg',
                                               'out_imgs/Edge_image_07_dex.jpg')
    def test_dex_pil_elephant(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/elephant.jpg',
                                               'out_imgs/elephant_dex.jpg')

    def test_dex_pil_bird_ornament(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/BirdOrnament.jpg',
                                               'out_imgs/BirdOrnament_dex.jpg')

    def test_dex_pil_hive01(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/hive01.png',
                                               'out_imgs/hive01_dex.png')

    def test_dex_pil_hive02(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/hive02.png',
                                               'out_imgs/hive02_dex.png')
    
    def test_dex_pil_hive02(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/hive03.png',
                                               'out_imgs/hive03_dex.png')

    def test_dex_pil_june(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/june.jpg',
                                               'out_imgs/june_dex.jpg')

    def test_dex_pil_lunch(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/lunch.jpg',
                                               'out_imgs/lunch_dex.jpg')

    def test_dex_pil_nutrition_table(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/nt_01.jpg',
                                               'out_imgs/nt_01_dex.jpg')

    def test_dex_pil_road_01(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/road_01.png',
                                               'out_imgs/road_01_dex.png')
        
    def test_dex_pil_road_02(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/road_02.png',
                                               'out_imgs/road_02_dex.png')
        
    def test_dex_pil_road_03(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/road_03.png',
                                               'out_imgs/road_03_dex.png')

    def test_dex_pil_road_04(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/road_04.png',
                                               'out_imgs/road_04_dex.png')

    def test_dex_pil_sudoku(self):
        cs3430_s24_hw06_uts.__test_dex_pil_img('imgs/sudoku.jpg',
                                               'out_imgs/sudoku_dex.jpg')
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()

    
