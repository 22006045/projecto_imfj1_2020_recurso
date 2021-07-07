import time
import math
import pygame

from quaternion import Quaternion
from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3

# Define a main function, just to keep things nice and tidy
def main():
    """Main function, it implements the application loop"""
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= Vector3(0, 0, 2)

    # Create a Pyramid and place it in a scene, at position (0,0,0) and with 5 Points
    obj1 = Object3d("TestObject")
    obj1.scale = Vector3(1, 1, 1)
    obj1.position = Vector3(0, 0, 0)
    obj1.mesh = Mesh.create_Pyramid(5)
    obj1.material = Material(Color(1, 0, 0, 1), "TestMaterial1")
    scene.add_object(obj1)

     # Specify the rotation of the object. It will rotate 15 degrees around the axis given,
    # every second

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)