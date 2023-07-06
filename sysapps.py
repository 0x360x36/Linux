import os

apps = ['zsh','kitty','python3-pip']

def update():
#this will upgrade and clean the system
    os.system('clear')
    commands = ['update','upgrade','autoremove','autoclean']
    for command in commands:
        os.system(f'sudo apt -y {command}')

def dev_env(apps):
#this will setup the dev environment
    os.system('clear')
    for app in apps:
        os.system(f'sudo apt install -y {app}')

def ohmyzsh():
#this will setup ohmyzsh
    os.system('clear')
    os.system('sudo apt install -y zsh')
    os.system('sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"')

os.system('clear')
print("----- System Control -----")
print("[1] Update the system")
print("[2] Setup the developer environment, this will install:")
for app in apps:
    print(f"    -> {app}")
print("[3] Set Oh-My-Zsh")

option = str(input("Choose an option: \n> "))

if option == '1':
    update()
elif option == '2':
    dev_env(apps)
elif option == '3':
    ohmyzsh()
else:
    os.system('clear')
    print('byee!')
    exit()