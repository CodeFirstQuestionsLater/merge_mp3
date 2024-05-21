#!/usr/bin/env python3

import os
import subprocess

# Get the current directory
current_directory = os.getcwd()

# Iterate over each item in the current directory
for item in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item)
    
    # Check if the item is a directory
    if os.path.isdir(item_path):
        # Construct the command
        output_file = f"{item}.mp3"
        command = [
            "python3", "merge_mp3.py",
            "-s",
            "-o", output_file,
            "-d", item_path
        ]
        
        # Execute the command
        subprocess.run(command)