#
# filename    : lab-136-argparse-os-shutil-del-folder.py
# Description :
# Docs        :
#               * https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
#               * https://docs.python.org/3/howto/argparse.html
# Requirements:
#               *
#

import argparse
import os, shutil

parser = argparse.ArgumentParser()
parser.add_argument("workspace_folder", help='folder to remove all files and subfolder contents')
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
args = parser.parse_args()
print(args)

if os.path.isdir(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if args.verbose:
            print(f'removing {file_path} ...')
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
else:
    print('Failed. Reason: folder "%s" does not exists!' % folder)