"""
@0x360x36
This scrip install a bundle of pentesting tools

"""

import subprocess

def update_system():
    """
    this function will update and clean
    the system
    """

    # Update and upgrade the system
    subprocess.check_call(['sudo', 'apt', 'update'])
    subprocess.check_call(['sudo', 'apt', 'upgrade', '-y'])
    subprocess.check_call(['sudo', 'apt', 'autoremove', '-y'])
    subprocess.check_call(['sudo', 'apt', 'autoclean', '-y'])


def install_tools():
    """
    This function installs a set of penetration testing tools on a Debian-based system.
    """
    tools = [
        'nmap',
        'sqlmap',
        'john',
        'hashcat',
        'rtl-433',
        'openvpn',
        'lynis',
        'bettercap',
        'wireshark',
        'httrack'
    ]
    subprocess.check_call(['sudo', 'apt', 'install', '-y'] + tools)

if __name__ == "__main__":
    # Update the system
    update_system()
    install_tools()
