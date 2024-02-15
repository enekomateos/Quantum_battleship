
## This file installs dependencies

from subprocess import check_output

def install_np():
    check_output("pip install numpy", shell=True)