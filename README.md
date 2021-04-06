# LUVMI-X Rover

Main repository for LUVMI-X rover on-board software.

## Prerequisites
### 1. Install Docker
Update the apt package index and install packages to allow apt to use a repository over HTTPS:
'''console
    sudo apt-get update
    sudo apt-get install \ apt-transport-https \ ca-certificates \ curl \ gnupg \ lsb-release
'''
    
Add Docker’s official GPG key then install the latest stable version of Docker Engine and containerd:
    
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg 
    echo \ "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io

Enable Docker:

    sudo usermod -aG docker <username>
    sudo systemctl enable docker.service

### 2. Install ROS 2
Add the ROS 2 apt repositories to your system:

    sudo apt update && sudo apt install curl gnupg2 lsb-release    
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -  
    sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
    
Install ROS 2:

    sudo apt update
    sudo apt install ros-foxy-desktop
    
Add the command to your shell startup script:

    echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

### 3. Add Extensions to Visual Code

Docker, Python and Remote Development

### 4. Setup Visual Code Environment

## First Run
Add personal public SSH Key in Gitlab (https://gitlab.spaceapplications.com/help/ssh/README#generating-a-new-ssh-key-pair)
Clone the repository using SSH.

Inside _packages_ folder enter the following commands:

    git submodule init
    git submodule update

Go to _Docker_ folder and run docker.sh:

    ./docker.sh

Countainer should be created now and you should be inside. Finish the installation the first time the container is executed by running:

    source finish_installation.sh

Go to _install_ folder change ownership to your local username and make the file _setup.sh_ executable. Run the _setup.sh_ script to install all dependencies for the virtual environment:

    ./setup.sh

## Docker
The software runs within a Docker container. To simplify its management 
(creating, starting and attaching to it) a helper script is
provided:

    .Docker/docker.sh
