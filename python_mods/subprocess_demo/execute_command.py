import os
import sys
import subprocess

from pathlib import Path

BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..\\..\\')
SCREENSHOT_PATH = BASE_PATH + 'tests\\ui\\screenshots'
WEBSITE_STATIC_PATH = BASE_PATH + 'website\\app\\static\\images\\'


def does_symlink_exist():
    exists = False
    symlink_path = WEBSITE_STATIC_PATH + 'screenshots'

    if Path(symlink_path).exists():
        if Path(symlink_path).is_symlink():
            exists = True

    return exists


def create_symlink():
    exists = does_symlink_exist()

    if exists:
        print('Symlink already exists. Hence exiting..')
        sys.exit()
    else:
        execute_command_for_symlink_3()


def execute_command_for_symlink(output):
    print('Creating symlink')
    command = ['powershell.exe', '-NoProfile',
               'New-Item', '-ItemType SymbolicLink',
               '-Path ', WEBSITE_STATIC_PATH, '-Name screenshots',
               '-Value ', SCREENSHOT_PATH]
    # symlink_path = WEBSITE_STATIC_PATH + 'screenshots'
    # command = 'mklink {} {}'.format(symlink_path, SCREENSHOT_PATH)
    try:
        output = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        print('subprocess CalledProcessError.output = ', e.output)
    print(output.decode())
    return output


def execute_command_for_symlink_2():
    import win32file

    symlink_path = WEBSITE_STATIC_PATH + 'screenshots'
    win32file.CreateSymbolicLink(symlink_path, SCREENSHOT_PATH)


def execute_command_for_symlink_3():
    from subprocess import call
    symlink_path = WEBSITE_STATIC_PATH + 'screenshots'
    call(['mklink', symlink_path, SCREENSHOT_PATH], shell=True)


if __name__ == '__main__':
    create_symlink()


