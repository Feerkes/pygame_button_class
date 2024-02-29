#pygame button class

import pygame

class button() :
    
    def __innit__(x, y, width, height, shape='rectange', color='(255, 0, 0)', texture='none') :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shape = shape
        self.color = color
        self.texture = texture
    
    