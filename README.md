# ECAM Computer Science Projects

Here are all the projects for the 2nd and 3rd year of Computer Science Engineering Bachelor at ECAM

# LUVMI-X Rover

Main repository for LUVMI-X rover on-board software.


## Docker
The software runs within a Docker container. To simplify its management 
(creating, starting and attaching to it) a helper script is
provided:

    .Docker/docker.sh

### First run
Finish the installation the first time the container is executed by running:

    source finish_installation.sh

## Prerequisites
### 1. Install docker:
Update the apt package index and install packages to allow apt to use a repository over HTTPS:

    sudo apt-get update
    
    sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
    
Add Docker’s official GPG key then install the latest version of Docker Engine and containerd:
    
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    
    echo \ "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    sudo apt-get update
    
    sudo apt-get install docker-ce docker-ce-cli containerd.io

### 2. Install Ros2
