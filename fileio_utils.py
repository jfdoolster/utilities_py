
import os
import glob

def clean_path(path: str) -> str:
    _path = path.replace('$HOME','~')
    _path = os.path.expanduser(_path)
    return _path

def unix_path(path: str) -> str:
    _path = clean_path(path)
    return os.path.normpath(_path).replace(os.sep, '/')

def absolute_path(path: str, unix_style=True) -> str:
    _path = clean_path(path)
    _path = os.path.abspath(_path)
    if unix_style:
        return unix_path(_path)
    return _path

def get_directory_files(directory: str, wildcard='*'):
    dir = absolute_path(directory)
    if not os.path.isdir(dir):
        print(f"{dir:s} does not exist")
        return list()
    return sorted(glob.glob(f"{dir:s}/{wildcard}"))

if __name__ == "__main__":
    path = '../../Documents/jfd_logs'
    print(unix_path(path))
    print(absolute_path(path, False))
    print(absolute_path(path, True))
    print(get_directory_files(path, wildcard="*"))
