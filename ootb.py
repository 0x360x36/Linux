import os
import sys
import getpass
import subprocess

def clear_terminal():
    subprocess.run(['clear'])

def system_updgrade():
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])

def ohmyzsh_install():
    system_updgrade()
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'zsh', 'curl'])
    subprocess.run(['chsh', '-s', '/bin/zsh'])
    subprocess.run(['sh', '-c', ' "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'])

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

def install_utilities():
    system_updgrade()
    programs = [
        'neovim',
        'neofetch',
        'nmap',
        'ranger'
    ]
    subprocess.run(['sudo', 'apt-get', 'install', '-y'] + programs )

def main():
    clear_terminal()
    print("--- OOTB ---\nWelcome to the Out-Of-The-Box (OOTB) installer for my custom settings DevEnv in WSL (Windows Subsystem for Linux)")
    print(
        f"[1] Install Oh-My-Zsh\n[2] Configure Git (Print Generated Public Key)\n[3] Install programs "
        )
    u_opt = input('-> ')
    if u_opt == '1':
        ohmyzsh_install()
    elif u_opt == '2':
        git_config()
    elif u_opt == '3':
        install_utilities()
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()