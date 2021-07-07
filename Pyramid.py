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

    # Specify the rotation of the object. It will rotate around the axis given, every second

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

     # Game loop, runs forever
    while True:
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        #Detect if key is pressed and rotate object
        if event.key == pygame.K_LEFT:
            angle = 0.1
            axis = Vector3(0, 1, 0)
            axis.normalize()
            ax = (axis * math.radians(angle) * 0.1)
            q = Quaternion.AngleAxis(axis, math.radians(angle) * 0.1)
            obj1.rotation = q * obj1.rotation

        #Detect if key is pressed and rotate object
        if event.key == pygame.K_RIGHT:
            angle = -0.1
            axis = Vector3(0, 1, 0)
            axis.normalize()
            ax = (axis * math.radians(angle) * 0.1)
            q = Quaternion.AngleAxis(axis, math.radians(angle) * 0.1)
            obj1.rotation = q * obj1.rotation

        #Detect if key is pressed and rotate object
        if event.key == pygame.K_UP:
            angle = 0.1
            axis = Vector3(1, 0, 0)
            axis.normalize()
            ax = (axis * math.radians(angle) * 0.1)
            q = Quaternion.AngleAxis(axis, math.radians(angle) * 0.1)
            obj1.rotation = q * obj1.rotation

        #Detect if key is pressed and rotate object
        if event.key == pygame.K_DOWN:
            angle = -0.1
            axis = Vector3(1, 0, 0)
            axis.normalize()
            ax = (axis * math.radians(angle) * 0.1)
            q = Quaternion.AngleAxis(axis, math.radians(angle) * 0.1)
            obj1.rotation = q * obj1.rotation

        #Detect if key is pressed and rotate object
        if event.key == pygame.K_PAGEUP:
            angle = 0.1
            axis = Vector3(0, 0, 2)
            axis.normalize()
            ax = (axis * math.radians(angle) * 0.1)
            q = Quaternion.AngleAxis(axis, math.radians(angle) * 0.1)
            obj1.rotation = q * obj1.rotation

        #Detect if key is pressed and rotate object
        if event.key == pygame.K_PAGEDOWN:
            angle = -0.1
            axis = Vector3(0, 0, 1)
            axis.normalize()
            ax = (axis * math.radians(angle) * 0.1)
            q = Quaternion.AngleAxis(axis, math.radians(angle) * 0.1)
            obj1.rotation = q * obj1.rotation

        #Detect if key is pressed and move object up relative to screen(+yAxis)
        if event.key == pygame.K_w:
            #Take coordinate x,y,z and add value to y.
            obj1.position=Vector3(obj1.position.x,obj1.position.y+0.001,obj1.position.z)

        #Detect if key is pressed and move object down relative to screen(-yAxis)
        if event.key == pygame.K_s:
            #Take coordinate x,y,z and add value to y.
            obj1.position=Vector3(obj1.position.x,obj1.position.y-0.001,obj1.position.z)

        #Detect if key is pressed and move object right relative to screen(+xAxis)
        if event.key == pygame.K_d:
            #Take coordinate x,y,z and add value to x.
            obj1.position=Vector3(obj1.position.x+0.001,obj1.position.y,obj1.position.z)

        #Detect if key is pressed and move object left relative to screen(-xAxis)
        if event.key == pygame.K_a:
            #Take coordinate x,y,z and add value to x.
            obj1.position=Vector3(obj1.position.x-0.001,obj1.position.y,obj1.position.z)

        #Detect if key is pressed and move object towards screen(+zAxis)
        if event.key == pygame.K_q:
            #Take coordinate x,y,z and add value to x.
            obj1.position=Vector3(obj1.position.x,obj1.position.y,obj1.position.z+0.001)

        #Detect if key is pressed and move object away from screen(-zAxis)
        if event.key == pygame.K_e:
            #Take coordinate x,y,z and add value to x.
            obj1.position=Vector3(obj1.position.x-0.001,obj1.position.y,obj1.position.z-0.001)
            
            
            
            

            

            

