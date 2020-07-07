import pygame
from math import sin, cos, sqrt
from Functions import normalize, SignedDistance, offScreen

class Ray:
    def __init__(self, x, y, angle, screen, color):
        self.position = [x, y]
        self.angle = angle
        self.screen = screen
        self.color = color
        self.x_position = 0
        self.y_position = 0
        
    def March(self, objects):
        counter = 0
        current_position = self.position
        pygame.draw.circle(self.screen, (255, 41, 120), self.position, 5)
        while counter < 100:
            record = 2000
            closest = None
            for obj in objects:
                distance = SignedDistance(current_position, obj, obj.radius)
                if distance < record:
                    record = distance
                    closest = obj
            
            if record < 1:
                break
            
            self.x_position = current_position[0] + cos(self.angle) * record
            self.y_position = current_position[1] + sin(self.angle) * record
            a_X = current_position[0] + cos(self.angle) * record
            a_Y = current_position[1] + sin(self.angle) * record
            pygame.draw.circle(self.screen, (0, 204, 37), (int(current_position[0]), int(current_position[1])), abs(int(record)), 1)
            
            pygame.draw.line(self.screen, self.color, (self.position[0], self.position[1]), (normalize(self.x_position) * a_X, normalize(self.y_position) * a_Y))
            current_position[0] = normalize(self.x_position) * a_X
            current_position[1] = normalize(self.x_position) * a_Y
            pygame.draw.circle(self.screen, self.color, (int(self.x_position), int(self.y_position)), 5)
            closest.display(self.screen, (130, 190, 41))
            
            if offScreen([self.x_position, self.y_position], 1280, 720):
                break
            if offScreen(current_position, 1280, 720):
                break
            
            counter += 1
            
            pygame.display.update()
            
            
            