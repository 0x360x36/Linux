uname -r
sudo apt search linux-headers-$(uname -r)

sudo apt install linux-headers-$(uname -r)

ls -l /usr/src/linux-headers-$(uname -r)
