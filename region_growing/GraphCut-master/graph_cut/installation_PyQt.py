import pip
from pip._internal import main as pipmain

def install_whl(path):
    pipmain(['install', path])


install_whl(r"C:\Users\DIDT03\Downloads\PyQt4-4.11.4-cp36-cp36m-win_amd64.whl")