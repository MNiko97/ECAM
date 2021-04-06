# LUVMI-X Rover
Main repository for LUVMI-X rover on-board software.

## Prerequisites
Operating System: tested on Ubuntu 20.04.02 LTS with python version 3.8.5

### Install Docker
Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```console
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```
    
Add Docker’s official GPG key then install the latest stable version of Docker Engine and container:
```console    
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg 
echo \ "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \ $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Enable Docker:
```console
sudo usermod -aG docker <username>
sudo systemctl enable docker.service
```

## Setup your coding environment (for Visual Code users)

Install the following extensions: 
Docker, Python and Remote Development

## First Run
Add personal public SSH Key in Gitlab (https://gitlab.spaceapplications.com/help/ssh/README#generating-a-new-ssh-key-pair)
Clone the repository using SSH.

Inside _packages_ folder enter the following commands (disclaimer: do not use --recursive flag if you arleady used it during the cloning process):
```console
git submodule update --init --recursive
```

Go to _Docker_ folder and run docker.sh:
```console
./docker.sh
```

Countainer should be created now and you should be inside. Finish the installation the first time the container is executed by running:
```console
source finish_installation.sh
```    

You can now build the packages and install the docker image (and all its dependencies) by running the following commands:
```console
colcon build --symlink-install
source install/setup.bash
```

## Docker
The software runs within a Docker container. To simplify its management 
(creating, starting and attaching to it) a helper script is
provided:
```console
.Docker/docker.sh
```
