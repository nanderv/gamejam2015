from cx_Freeze import setup, Executable

exe=Executable(
     script="game.py",
     base="Win32Gui",
     )
includefiles=["Sprite-0001.png","Sprite-0002.png","tiles_20.png"]
includes=["json_map"]
excludes=[]
packages=[]
setup(

     version = "0.0",
     description = "No Description",
     author = "Name",
     name = "App name",
     options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables = [exe]
     )