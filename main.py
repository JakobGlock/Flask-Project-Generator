#!/usr/bin/python3

import os
import argparse
import json
import subprocess

# Helpers
# Create a file
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

# Variables
createFiles = ['/README.md', '/requirements.txt', '/run.py', '/app/__init__.py', '/app/models.py', '/app/routes.py', '/app/templates/index.html']

parser = argparse.ArgumentParser()
parser.add_argument("projectName")
args = parser.parse_args()

projectName = args.projectName

# Check to see if the project folder already exists
if os.path.isdir(projectName) is not True:

    # Create folder structure
    print(f"Creating project in the folder: {projectName}")
    os.makedirs(projectName + "/app/static")
    os.makedirs(projectName + "/app/templates")

    print("\nCreated files:")
    # Create files
    for file in createFiles:
        touch(projectName + file)
        print("\t" + projectName + file)

    # Insert template code
    print("\nLoading in template data....")
    with open('data.json') as file:
        t = json.load(file)
        for key, value in t.items():
            with open(projectName + key, 'w') as f:
                f.write(value)
    print("....Loading DONE\n")

    print("Creating virutal environment....")
    subprocess.call(f"python3 -m venv {projectName}/venv", shell=True)
    print("VENV created\n")

    print("Installing packages with pip3....\n")
    subprocess.call([f"{projectName}/venv/bin/python3", "-m", "pip", "install", "-r", f"{projectName}/requirements.txt"])
    print("\n....Pip3 install done")

    print("\nProject setup complete")
    print(f"\nGo to the project folder and activate the venv using:\n\tsource venv/bin/activate\n\nThen run the follwing command to start the server:\n\tpython3 run.py\n\nDont forget to setup a database and put in the correct credentials in to __init__.py\n\nHave fun\n\n:)")
else:
    print("Project folder already exists")
