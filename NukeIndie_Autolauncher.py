import os
import subprocess

#You Need to change your program path
def open_nkind_file(file_path):
    nuke_exe = "C:\\Program Files\\Nuke13.2v4\\Nuke13.2.exe"
    subprocess.Popen([nuke_exe, "--indie", file_path], shell=True)

# Example usage
file_path = "Project_Path\\filename.nkind"
open_nkind_file(file_path)

#This code make read .nkind(Nuke Indie file) automatically and launch in Nuke Indie. 
