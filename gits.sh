
read -p "Git Config UserName = " your_username
your_username=${your_username:-$USER}

git config --global user.name "'$username'"

read -p "Git Config UserEmail = " username
username=${username:-$USER}

echo "Email: "
read your_email
ssh-keygen -t ed25519 -C "$your_email"

eval "$(ssh-agent -s)"

ssh-add /home/$USER/.ssh/id_ed25519

# Your identification has been saved in ~/.ssh/id_ed25519
# Your public key has been saved in ~/.ssh/id_ed25519.pub

cat /home/$USER/.ssh/id_ed25519.pub 