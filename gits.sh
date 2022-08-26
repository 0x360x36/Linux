
echo "Email: "
read your_email
ssh-keygen -t ed25519 -C "$your_email"

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_ed25519

# Your identification has been saved in ~/.ssh/id_ed25519
# Your public key has been saved in ~/.ssh/id_ed25519.pub

cat ~/.ssh/id_ed25519.pub 