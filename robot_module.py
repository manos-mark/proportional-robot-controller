from typing import ForwardRef
import math
import numpy as np

class Robot():
    def __init__(self, robot_name="Test Robot", max_speed=0.3, initial_pos=[0, 0]):
        self.name = robot_name
        self.max_speed = max_speed
        self.initial_pos = initial_pos
        self.current_pos = np.array(self.initial_pos)
        self.rotational_speed = 0 # ω
        self.forward_speed = 0 # Vf

    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def current_pos(self):
        return self.__current_pos

    @current_pos.setter
    def current_pos(self, pos):
        self.__current_pos = pos

    @property
    def forward_speed(self):
        return self.__forward_speed
    
    @forward_speed.setter
    def forward_speed(self, forward_speed):
        self.__forward_speed = forward_speed if forward_speed < self.max_speed else self.max_speed

    @property
    def rotational_speed(self):
        return self.__rotational_speed
    
    @forward_speed.setter
    def rotational_speed(self, rotational_speed):
        self.__rotational_speed = rotational_speed if rotational_speed < self.max_speed else self.max_speed

    def update_position(self, velocity):
        """ 
        Update the robot's current position

        Parameters:
            velocity (float): Velocity
        """
        self.__current_pos = self.__current_pos + velocity
