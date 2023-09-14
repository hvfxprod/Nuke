#누크 일부 버전에서 Indie파일이 Indie 모드로 실행이 안되는 문제가 있었음.
#기존에는 레지스트리 수정을 통해서 nuke를 nukex로 실행하는 방법이 있었지만 인디는 레지스트리에서 찾지 못했음
#따라 프로젝트 경로를 작성하여 아이콘 클릭시 자동으로 프로젝트를 실행해주는 스크립트임.
#인디로 자동실행하는 방법은 나와있음. 누크 공식 홈페이지에 기재되어 있고, 이 파일은 임시적으로 바로가기 파일로 가게 해 주는것이라고 생각하면 됨.
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
