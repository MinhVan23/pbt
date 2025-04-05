#!/usr/bin/python3

import sys
import os
import shutil
import subprocess

setup_dir = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(setup_dir, "src")
wrapper_path = os.path.join(setup_dir, "pbt")
program_dir = os.path.expanduser("~/.local/share/pbt")
data_dir = os.path.expanduser('~/pbt')

def install():
    if os.path.exists(f'/usr/local/bin/pbt'):
        print('Error: pbt is already installed.')
        return
    print('Installing pbt...')

    shutil.copytree(src_dir, os.path.expanduser("~/.local/share/pbt"), dirs_exist_ok=True)
    wrapper_content = f"""#!/bin/bash
python3 "{program_dir}/pbt.py" "$@"
"""
    with open(wrapper_path, 'w') as file:
        file.write(wrapper_content)

    command = f"sudo mv {wrapper_path} /usr/local/bin"
    subprocess.run(command, shell=True)
    command = f'sudo chmod +x /usr/local/bin/pbt'
    subprocess.run(command, shell=True)

    print(f'Creating folder to store user\'s data at {data_dir}')
    os.mkdir(data_dir)
    os.mkdir(os.path.join(data_dir, 'exports'))
    print('pbt is installed successfully at /usr/bin/local/pbt!')

def uninstall():
    if not os.path.exists(f'/usr/local/bin/pbt'):
        print('Error: pbt is not installed.')
        return
    print('Uninstalling pbt...')

    command = 'sudo rm /usr/local/bin/pbt'
    subprocess.run(command, shell=True)
    shutil.rmtree(program_dir)
    print('Removing user\'s data folder')

    shutil.rmtree(data_dir)

    print('pbt is uninstalled successfully.')

def help():
    print("""
Usage: setup.py [option]

Options:
    --install     install pbt
    --uninstall   uninstall pbt
    --help        show this help message
          """)

option = sys.argv[1] if len(sys.argv) > 1 else None
if option == '--install':
    install()
elif option == '--uninstall':
    uninstall()
elif option == '--help':
    help()
else:
    print("Unknown option.")
    help()