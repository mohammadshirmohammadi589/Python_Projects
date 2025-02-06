import os
import logging
import argparse

# Set up logging
logging.basicConfig(filename='cli_logs.log', level=logging.INFO)

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Python Command Line Interface Tool')
parser.add_argument('command', help='The command to be executed')
parser.add_argument('path', nargs='?', default='.', help='The path for file manipulation or directory navigation')

# Parse the arguments
args = parser.parse_args()

# Log the command usage
logging.info(f'Command: {args.command}, Path: {args.path}')

# Execute the command
if args.command == 'list':
    files = os.listdir(args.path)
    for file in files:
        print(file)
elif args.command == 'create_file':
    with open(os.path.join(args.path, 'new_file.txt'), 'w') as f:
        pass
    print('File created successfully')
elif args.command == 'create_dir':
    os.makedirs(os.path.join(args.path, 'new_directory'))
    print('Directory created successfully')
elif args.command == 'delete_file':
    os.remove(os.path.join(args.path, 'file_to_delete.txt'))
    print('File deleted successfully')
elif args.command == 'delete_dir':
    os.rmdir(os.path.join(args.path, 'directory_to_delete'))
    print('Directory deleted successfully')
else:
    print('Invalid command')

import shutil

# Add the new commands to the CLI tool
if args.command == 'ls':
    files = os.listdir(args.path)
    for file in files:
        print(file)
elif args.command == 'cd':
    os.chdir(args.path)
    print(f'Changed directory to {args.path}')
elif args.command == 'mkdir':
    os.makedirs(args.path)
    print('Directory created successfully')
elif args.command == 'rmdir':
    os.rmdir(args.path)
    print('Directory deleted successfully')
elif args.command == 'rm':
    os.remove(args.path)
    print('File deleted successfully')
elif args.command == 'rm -r':
    shutil.rmtree(args.path)
    print('Directory and its contents deleted successfully')
elif args.command == 'cp':
    source, destination = args.path.split()
    if os.path.isdir(source):
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)
    print('File or directory copied successfully')
elif args.command == 'mv':
    source, destination = args.path.split()
    shutil.move(source, destination)
    print('File or directory moved successfully')
elif args.command == 'find':
    path, pattern = args.path.split()
    for root, dirs, files in os.walk(path):
        for file in files:
            if pattern in file:
                print(os.path.join(root, file))
elif args.command == 'cat':
    with open(args.path, 'r') as f:
        print(f.read())
else:
    print('Invalid command')


import argparse
import datetime
import logging

# Define the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('command_logs.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Define the command functions
def command1(args):
    # TODO: Implement command1 logic here
    logger.info(f"Command1 executed with arguments {args} at {datetime.datetime.now()}")
    print("Command1 executed successfully")

def command2(args):
    # TODO: Implement command2 logic here
    logger.info(f"Command2 executed with arguments {args} at {datetime.datetime.now()}")
    print("Command2 executed successfully")

# Parse command line arguments
parser = argparse.ArgumentParser(description='Sample command line tool')
subparsers = parser.add_subparsers()

# Command1
parser_command1 = subparsers.add_parser('command1', help='Execute command1')
parser_command1.add_argument('arg1', help='Argument 1 for command1')
parser_command1.set_defaults(func=command1)
# Command2
parser_command2 = subparsers.add_parser('command2', help='Execute command2')
parser_command2.add_argument('arg1', help='Argument 1 for command2')
parser_command2.add_argument('arg2', help='Argument 2 for command2')
parser_command2.set_defaults(func=command2)

# Parse the arguments and execute the command
args = parser.parse_args()
try:
    args.func(args)
    logger.info(f"Command executed successfully at {datetime.datetime.now()}")
except Exception as e:
    logger.error(f"Command execution failed: {e} at {datetime.datetime.now()}")
    print(f"Command execution failed: {e}")


import os

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"{folder_name} folder created successfully.")
    except FileExistsError:
        print(f"{folder_name} folder already exists.")




import re

def search_in_file(file_name, pattern):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            matches = re.findall(pattern, content)
            if matches:
                return matches
            else:
                return "No match found."
    except FileNotFoundError:
        return f"{file_name} not found."