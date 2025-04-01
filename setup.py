import sys
import os
import shutil
import subprocess

pbt_path = os.path.abspath(__file__)
data_dir = os.path.expanduser('~/pbt')
data_path = os.path.expanduser('~/pbt/data.json')

def install():
    if os.path.exists(f'/usr/bin/local/pbt'):
        print('Error: pbt is already installed.')
        print('Error: pbt is uninstalled unsuccessfully.')
        return
    print('Installing pbt...')
    command = f'sudo cp {pbt_path} /usr/bin/local'
    subprocess.run(command)
    os.mkdir(pbt_path)
    os.mkdir(data_path)
    print(f'Create folder to store user\'s data at {data_dir}')
    print('pbt is installed successfully at /usr/bin/local/pbt!')

def uninstall():
    if not os.path.exists(f'/usr/bin/local/pbt'):
        print('Error: pbt is not installed.')
        print('pbt is uninstalled unsuccessfully.')
        return
    print('Uninstalling pbt...')
    command = 'sudo rm /usr/local/bin/pbt'
    subprocess.run(command)
    shutil.rmtree(pbt_path)
    print('Remove user\'s data folder')
    print('pbt is uninstalled successfully.')

command = sys.argv[1] if len(sys.argv) > 1 else None
if command == 'install':
    install()
elif command == 'uninstall':
    uninstall()
elif command == '--help':
    help()
else:
    print('Error: Unknown setup option or incorrect syntax. Use --help to list options.')