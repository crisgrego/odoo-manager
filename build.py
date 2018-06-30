# python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
from PyQt5 import uic

def get_target(dir, name):
    return ('./package/ui/widgets', name)

uic.compileUiDir('./views', recurse=True, map=get_target)


