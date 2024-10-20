import os
import sys
import getpass
import subprocess

def clear_terminal():
    subprocess.run(['clear'])

def system_updgrade():
    subprocess.run(['sudo', 'apt-get', 'update', '-y'])
    subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])

def git_config():
    git_username = input(f"Git Config UserName [{getpass.getuser()}]: ") or getpass.getuser()
    git_email = input(f"Git Config UserEmail [{getpass.getuser()}@{os.uname().nodename}]: ") or f"{getpass.getuser()}@{os.uname().nodename}"

    subprocess.run(["git", "config", "--global", "user.name", git_username])
    subprocess.run(["git", "config", "--global", "user.email", git_email])

    ssh_key_path = os.path.expanduser("~/.ssh/id_ed25519")
    if not os.path.exists(ssh_key_path):
        subprocess.run(["ssh-keygen", "-t", "ed25519", "-C", git_email])

    subprocess.run(["eval", "$(ssh-agent -s)"], shell=True)
    subprocess.run(["ssh-add", ssh_key_path])

    with open(f"{ssh_key_path}.pub", "r") as public_key_file:
        public_key = public_key_file.read()
        print(f"\nYour public SSH key is:\n\n{public_key}\n")

def install_base_utilities():
    system_updgrade()
    programs = [
        'neovim',
        'neofetch',
        'openssh-server',
        'zsh',
        'python3-pip'
    ]
    print("Installing the following programs:")
    for p in programs:
        print(f'- {p}')

    subprocess.run(['sudo', 'apt-get', 'install', '-y'] + programs )

def main():
    quitprogr = False
    while quitprogr == False:
        clear_terminal()
        print("--- OOTB ---\nWelcome to the Out-Of-The-Box (OOTB) installer for my custom DevEnv settings in a Debian based distro")
        print(f"[1] Updgrade System (Update && Upgrade)\n[2] Install Base Utilities ")
        u_opt = input('-> ')
        if u_opt == '1':
            system_updgrade()
        elif u_opt == '2':
            install_base_utilities()
        else:
            quitprogr = True
    sys.exit(0)

if __name__ == "__main__":
    main()
