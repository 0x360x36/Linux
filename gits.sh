
read -p "Git Config UserName = " your_username
your_username=${your_username:-$USER}

read -p "Git Config UserEmail = " your_email
your_email=${your_email:-$USER}

git config --global user.name "'$your_username'"

git config --global user.email "'$your_email'"

ssh-keygen -t ed25519 -C "'$your_email'"

eval "$(ssh-agent -s)"

ssh-add /home/$USER/.ssh/id_ed25519

# Your identification has been saved in ~/.ssh/id_ed25519
# Your public key has been saved in ~/.ssh/id_ed25519.pub

cat /home/$USER/.ssh/id_ed25519.pub 