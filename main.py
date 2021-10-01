import time
import matplotlib.pyplot as plt
import numpy as np

from robot_module import Robot
from controller_module import Controller

# K is the constant we adjust to change robot behavior
K = 0.3

# Δt - constant
iteration_time_sec = 0.001

# Target position
target_pos = np.array([-1, -2])

# Initialize a Robot object
robot = Robot( "STUPIDO", 0.03, np.array([1, 1]))

# Initialize the Controler
controller = Controller(K, K)

current_time = time.time()

theta = 0

def move_robot():
    distance_to_target = controller.distance_to_target(robot.current_pos, target_pos)
    if distance_to_target < 0.01:
        print('Target reached!')
        return False
    else:
        # Compute forward and rotation speed with controller
        # set speed to robot
        global current_time
        t_k = current_time
        time.sleep(iteration_time_sec)
        current_time = time.time()

        dt = current_time - t_k

        # Update robot pos with t_k and current_time
        global theta
        theta, velocity, rotational_speed, forward_speed = controller.control(distance_to_target, theta, dt, robot.current_pos, target_pos)

        robot.rotational_speed = rotational_speed
        robot.forward_speed = forward_speed
        robot.update_position(velocity)

        # print(f"distance_to_target: {distance_to_target} \t dt:{dt} \t  Current Pos:{robot.current_pos} \t Theta error:{theta_error} ")
        return True

#### Testing code
# Interactive plot initialization
plt.ion()
fig, ax = plt.subplots()
plot_points = ax.scatter([], [])
plt.grid()
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
it = 0
#### End of testing code
while True:
    x,y = robot.current_pos
    #### Testing code
    ## We add a new point to the array of point in the interactive plot
    point = np.array([[x, y]])
    array = plot_points.get_offsets()
    array = np.append(array, point, axis=0)
    plot_points.set_offsets(array)
    ## We change the axis limits to see al the points
    ax.set_xlim(array[:, 0].min() - 0.5, array[:,0].max() + 0.5)
    ax.set_ylim(array[:, 1].min() - 0.5, array[:, 1].max() + 0.5)
    plt.title("Trajectory plot\nIteration #: {}".format(it))
    it += 1
    fig.canvas.draw()
    ## We require this line to let the plot update
    plt.pause(0.001)
    #### End of testing code
    
    if not move_robot():
        break

 ### OUTSIDE YOUR WHILE LOOP
#### Testing code
plt.ioff()
plt.close()
#### END of testing code