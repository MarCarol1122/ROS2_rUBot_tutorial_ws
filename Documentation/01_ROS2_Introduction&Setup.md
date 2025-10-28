# **ROS 2 Humble: An Introduction__**

In this section we will:
- learn what is ROS
- Setup a usefull working ROS environment
- Practice main concepts with Turtlesim robot

## **What is ROS?**

ROS (Robot Operating System) is not a traditional operating system, but a flexible framework for writing robot software. It's a collection of tools, libraries, and conventions that simplify the task of creating complex and robust robot behavior across a wide variety of robotic platforms.

Interesting references for courses:
- Edouard Renard: https://www.udemy.com/course/ros2-for-beginners/learn/lecture/20260476#overview
- https://www.udemy.com/course/learn-ros2-as-a-ros1-developer-and-migrate-your-ros-projects/learn/lecture/22003074#overview

And the ROS2 reference sites:
- https://docs.ros.org/
- https://docs.ros.org/en/humble/

ROS1 is close to finish and you can switch to ROS2
![](./Images/01_ROS2_setup/01_ROS2_time.png)

The main differences are:
![](./Images/01_ROS2_setup/03_ROS2_dif.png)

ROS2 is a very good choice.

**The Origin of ROS**

ROS originated in 2007 at Stanford University's in Stanford AI Laboratory (SAIL) as part of the Stanford Artificial Intelligence Robot (STAIR) project. Later, development transitioned to Willow Garage. 

ROS 2 was developed to address limitations in ROS 1, particularly concerning real-time performance, multi-robot systems, and production-level deployments.

**Why is it Useful?**

ROS 2 provides numerous benefits for robotics development:

- Hardware Abstraction: Enables to be used in different robot hardware (PC, Arduino board, mobile phone, etc.).
- Code Reusability: Facilitates the use of existing ROS packages and libraries from 3rd parties.
- Modularity: Enables the development of modular and maintainable code.
- Community Support: Offers access to a large and active community.
- Production Readiness: Designed for robust and reliable deployments.
- Robustness in terms of communication.
- Development Tools: Includes tools for visualization, debugging, and data logging (e.g., Rviz, ros2 bag).

**How it Works**

ROS 2 operates through a network of nodes that communicate using messages. A big project can be structured in a group of different nodes, each node contains a functionality and shares information with other nodes.

Here's a basic overview: Picture from ROS Official documentation: https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html
![](./Images/01_ROS2_setup/04_Topic-MultiplePublisherandMultipleSubscriber.gif)
  
- Nodes: Independent processes that perform specific tasks.
- Topics: Named communication channels where nodes publish and subscribe to messages.
- Messages: Data structures defined in .msg files, used to exchange information.
- DDS (Data Distribution Service): The middleware layer that handles the communication between nodes.
- Services and Actions: Mechanisms for request/response communication and long-running tasks with feedback.

## **Setup a usefull working ROS environment**

You can use the ROS environment developed by "The Construct" (https://app.theconstructsim.com/), enterprise working on ROS academia and development and located in Barcelona.
- Open the link: https://app.theconstructsim.com/
- Create a free user account
- Select "myRosjects"
![](./Images/01_ROS2_setup/05_myRosjects.png)
- Create a New Project: Select ROS2_Humble, create from the scratch and choose a name (i.e. ROS2_Humble)
![](./Images/01_ROS2_setup/06_Rosject.png)
You will have 2GB Virtual machine with Ubuntu 22 and ROS2 Humble installed for free!!

**Prepare your Workspace**

When working in Laboratory groups, we suggest you:
- One student plays the role of `Director`. This student makes a "Fork" of the Professor's github project.
- The `Director` accept the other students as `Collaborators`
![](./Images/01_ROS2_setup/07_github_collaborators.png)
- Then the `Collaborators` will make a "fork" of the `Director`'s github project.
- The `Collaborators` will be able to update the github `Director`'s project and participate on the project generation

To work on the project (during lab sessions or for homework at home), each student has to clone the `Director`'s github project in the `TheConstruct working environment`.
- Open your ROS2 Humble environment:  https://app.theconstructsim.com/
- Open your created ROS2_Humble Rosject project
- Clone your forked `Director`'s github project
  ```shell
  cd /home/user
  git clone https://github.com/director_username/ROS2_rUBot_tutorial_ws
  cd ROS2_rUBot_tutorial_ws
  colcon build
  ```
- If the compilation process returns warnings on "Deprecated setup tools". Install setup tools version 58.2.0 (last version to work with ros2 python packages without any warnings):
    ````shell
    sudo apt install python3-pip
    pip3 list | grep setuptools
    pip3 install setuptools==58.2.0
    ````
- If the compilation process returns wardings on PREFIX_PATH:
    ````shell
    unset COLCON_PREFIX_PATH
    unset AMENT_PREFIX_PATH
    unset CMAKE_PREFIX_PATH
    cd ~/ROS2_rUBot_tutorial_ws
    rm -rf build/ install/ log/
    colcon build
    ````
- Open .bashrc file (from user) with VS Code (open file...)
- Add the lines (review the exact name of your repository):
    ```xml
    source /opt/ros/humble/setup.bash
    source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
    source /home/user/ROS2_rUBot_tutorial_ws/install/setup.bash
    cd /home/user/ROS2_rUBot_tutorial_ws
    git config --global user.email "xxx@alumnes.ub.edu"
    git config --global user.name "your_github_username"
    ```
    > Include the name an email you have used to create your github account
You are ready to work with your repository for this session!

**Repository syncronisation**

The objective is to update the changes you have made, when working in ROS2 environment, in your github repository.

- Access to the TheConstruct environment local repository:
  ````shell
  cd /home/user/ROS2_rUBot_tutorial_ws
  ````
- Update the local repository with possible changes in github origin repository
  ````shell
  git pull
  ````
- You can work with your local repository for the speciffic project session
- Once you have finished and you want to syncronize the changes you have made and update the github origin repository, type:
  ````shell
  git add .
  git commit -m "Message"
  git push
  ````
- You will have to specify the Username and Password (Personal Access Token you have generated)

To obtain the **PAT** in github follow the instructions:

  - Log in to GitHub
  - Go to Developer Settings
  - Select Personal Access Tokens: Choose Tokens (classic)
  - Click Generate new token (classic) and configure it:
    - Add a note to describe the purpose of the token, e.g., "ROS repo sync."
    - Set the expiration (e.g., 30 days, 60 days, or no expiration).
    - Under Scopes, select the permissions required:
      - For repository sync, you usually need: repo (full control of private repositories)
    - Click Generate token
  - Once the token is generated, copy it immediately. You won't be able to see it again after leaving the page.

Your github origin repository has been updated!

## **Practice ROS2 with Turtlesim**

In this section we will practice the ROS2 concepts with a very simple and useful turtlesim robot.

Documentation:
- https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html

**Turtlesim environment**

Turtlesim is a package that contains a 2D turtle robot simulation and is a good opportunity to start working with ROS2.

We will start turtlesim node with:
```shell
ros2 run turtlesim turtlesim_node
```
![](./Images/01_ROS2_setup/08_turtlesim.png)

You can see the nodes, and their associated topics, services, and actions:
````shell
ros2 node list
ros2 topic list
ros2 service list
ros2 action list
````
![](./Images/01_ROS2_setup/08_turtlesim_node.png)

To see the **information about the nodes, topics and messages**, type:

```shell
ros2 node info /turtlesim
ros2 topic info /turtle1/cmd_vel
ros2 topic info /turtle1/pose
```
In order **to see the message structure**, type:
```shell
ros2 interface show geometry_msgs/msg/Twist
ros2 interface show turtlesim/msg/Pose 
```
you can also find the message structure in google: "geometry_msgs/Twist"

In order **to write a message to a topic** we have different options:
- we can **publish directly to the topic**: for exemple to publish a Twist type message with a rate of 1Hz to define a circle, type:

```shell
ros2 topic pub -r 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 2.0}}"
```

![](./Images/01_ROS2_setup/09_turtlesim_pub.png)

- or we will start another node to control the turtlesim robot:
```shell
ros2 run turtlesim turtle_teleop_key
```
![](./Images/01_ROS2_setup/10_turtlesim_key.png)

Use the arrow keys on your keyboard to control the turtle. It will move around the screen, using its attached “pen” to draw the path it followed so far.

In order **to listen a message from a topic**:
```shell
ros2 topic echo /turtle1/pose
ros2 topic echo /turtle1/cmd_vel
```

We can use "rqt_graph" and "rqt_plot" to se the nodes-topics structure and the message values

```shell
rqt_graph
rqt_plot
```

![](./Images/01_ROS2_setup/11_turtlesim_rqt.png)

