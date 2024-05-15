import sys
import inspect
import re

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

def DISPLAY(info:str, msg:str, fname:bool, slen=6):
    while len(info) < slen+1:
        info+=' '
    if len(info) > slen:
        info = info[:slen]

    if   'info' in info.lower(): info=str(bcolors.HEADER  + info.upper() + bcolors.ENDC)
    elif 'warn' in info.lower(): info=str(bcolors.WARNING + info.upper() + bcolors.ENDC)
    elif 'fail' in info.lower(): info=str(bcolors.FAIL    + info.upper() + bcolors.ENDC)
    elif 'pass' in info.lower(): info=str(bcolors.OKGREEN + info.upper() + bcolors.ENDC)
    else: info=str(info.upper() + bcolors.ENDC)

    PRINT = f"{info:{slen}s}: {msg:s}"
    if (fname):
        FNAME = inspect.stack()[2].function
        if (FNAME.lower() not in ['<module>']):
            FNAME = bcolors.BOLD  + f"{FNAME:s}()"+ bcolors.ENDC
            PRINT = f"{info:{slen}s}: [{FNAME:s}] {msg:s}"
    print(PRINT)
    return escape_ansi(PRINT)

def INFO(msg:str="", show_func:bool=True, TYPE:str='INFO'):
    return DISPLAY(TYPE, msg, fname=show_func)

def WARNING(msg:str="", show_func:bool=True):
    return DISPLAY('WARN', msg, fname=show_func)

def ERROR(msg:str="", show_func:bool=True, force_exit:bool=True):
    s = DISPLAY('FAIL', msg, fname=show_func)
    if force_exit:
        print("Exiting...")
        sys.exit()
    return s

def SUCCESS(msg:str="", show_func:bool=True):
    return DISPLAY('PASS', msg, fname=show_func)