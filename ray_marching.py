# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:05:02 2020

@author: moussa.rozzi
"""

import pygame
import os
from Boundary import Boundary
from random import randint
from ray import Ray

os.environ["SDL_VIDEO_CENTERED"] = '1'

width, height = 1280,720
size = (width,height)

white, black = (255,255,255),(0,0,0)

#pygame configs

pygame.init()
pygame.display.set_caption("2D raymarching")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

objects = []
object_count = 10
angle = 0
screen_offset = 50

for i in range(object_count):
    obj = Boundary(randint(screen_offset, width-screen_offset), randint(screen_offset, height-screen_offset), randint(10,100))
    objects.append(obj)
    
run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    ray = Ray(width//2, height//2,0, screen, white)
    ray.angle = angle
    screen.fill(black)
            
    for obj in objects:
        obj.display(screen, white)
        
    ray.March(objects)
    angle += 0.005
        
pygame.quit()
    
