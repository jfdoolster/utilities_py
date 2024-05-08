
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

def get_directory_files(directory: str, wildcard='*', unix_style=True):
    dir = absolute_path(directory)
    if not os.path.isdir(dir):
        print(f"{dir:s} does not exist")
        return list()
    files = sorted(glob.glob(os.path.join(dir, wildcard)))
    if unix_style:
        files = [unix_path(f) for f in files]
    return files

if __name__ == "__main__":
    path = '../../Documents/jfd_vault'
    print(unix_path(path))
    print(absolute_path(path, True))
    print(get_directory_files(path, wildcard="*"))
    print()
    path = '$HOME/Documents/jfd_vault'
    print(unix_path(path))
    print(absolute_path(path, True))
    print(get_directory_files(path, wildcard="*"))