
import os
import glob

def unix_path(path: str) -> str:
    _path = path.replace('$HOME','~')
    return os.path.normpath(_path).replace(os.sep, '/')

def absolute_path(path: str, unix_style=True) -> str:
    _path = path.replace('$HOME','~')
    _path = os.path.expanduser(_path)
    if unix_style:
        return unix_path(os.path.abspath(_path))
    return os.path.abspath(_path)

def get_directory_files(directory: str, wildcard='*'):
    dir = absolute_path(directory)

    if not os.path.isdir(dir):
        print(f"{dir:s} does not exist")
        return list()

    return sorted(glob.glob(f"{dir:s}/{wildcard}"))

if __name__ == "__main__":
    path = '$HOME'
    print(unix_path(path))
    print(absolute_path(path, False))
    print(absolute_path(path, True))
    print(get_directory_files(path, wildcard="*.png"))
