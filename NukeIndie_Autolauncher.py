#누크 일부 버전에서 Indie파일이 Indie 모드로 실행이 안되는 문제가 있었음.
#기존에는 레지스트리 수정을 통해서 nuke를 nukex로 실행하는 방법이 있었지만 인디는 레지스트리에서 찾지 못했음
#따라 프로젝트 경로를 작성하여 아이콘 클릭시 자동으로 프로젝트를 실행해주는 스크립트임.
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
