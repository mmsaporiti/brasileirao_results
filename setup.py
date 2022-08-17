from cx_Freeze import setup, Executable

base = None

executables = [Executable("bolao_brasileiro_player.py", base=base)]

packages = ["idna", "pandas"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Marcos Saporiti",
    options = options,
    version = "0.1",
    description = 'Bolão do Brasileirão',
    executables = executables
)