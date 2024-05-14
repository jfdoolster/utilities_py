

import os, sys

def realtive_to_file(relative_path:str):
    print(__file__)
    _path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path)).replace(os.sep, '/')
    print(_path)
    sys.path.append(_path)