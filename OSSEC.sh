apt-get install build-essential make zlib1g-dev libpcre2-dev libevent-dev libssl-dev
wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo bash
apt-get update
apt-get install ossec-hids-server
