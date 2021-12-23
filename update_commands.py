from shutil import copyfile
import os

TRIGGERCMD_FOLDER = 'C:\\Users\\gmont\\.TRIGGERcmdData'
LOCAL_FOLDER = 'triggercmd_commands'
COMMANDS_FILE = 'commands.json'
COMMANDS_BACKUP_FILE = 'commands.old.json'

triggercmd_file = os.path.join(TRIGGERCMD_FOLDER, COMMANDS_FILE)
local_file = os.path.join(LOCAL_FOLDER, COMMANDS_FILE)


def create_backup(dst):
    original_file = os.path.join(dst, COMMANDS_FILE)
    backup_file = os.path.join(dst, COMMANDS_BACKUP_FILE)

    # delete old backup
    if os.path.exists(backup_file):
        os.remove(backup_file)

    copyfile(original_file, backup_file)


def update_commands(dst):
    if dst == LOCAL_FOLDER:
        copyfile(triggercmd_file, local_file)
    else:
        copyfile(local_file, triggercmd_file)


def main():
    triggercmd_mdate = os.path.getmtime(triggercmd_file)
    local_mdate = os.path.getmtime(local_file)

    if local_mdate > triggercmd_mdate:
        print('copying local file to triggercmd')
        create_backup(TRIGGERCMD_FOLDER)
        update_commands(TRIGGERCMD_FOLDER)
    else:
        print('copying triggercmd to here')
        create_backup(LOCAL_FOLDER)
        update_commands(LOCAL_FOLDER)


if __name__ == '__main__':
    main()
