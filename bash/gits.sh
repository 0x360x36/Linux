#!/bin/bash

# Prompt the user for their Git username and email
read -rp "Git Config UserName [$USER]: " git_username
read -rp "Git Config UserEmail [$USER@$(hostname)]: " git_email

# Use the default username and email if the user did not enter any values
git_username=${git_username:-$USER}
git_email=${git_email:-$USER@$(hostname)}

# Set the user's Git username and email in the global Git configuration
git config --global user.name "$git_username"
git config --global user.email "$git_email"

# Generate an Ed25519 SSH key pair if one does not exist
if [ ! -f ~/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -C "$git_email"
fi

# Add the private key to the SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Display the public key
printf "\nYour public SSH key is:\n\n"
cat ~/.ssh/id_ed25519.pub
printf "\n"