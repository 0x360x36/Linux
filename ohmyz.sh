#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install -y zsh wget

chsh -s $(which zsh)

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
