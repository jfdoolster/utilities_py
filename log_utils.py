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

def escape_ansi(line:str) -> str:
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

def DISPLAY(hdr:str, msg:str, show_func:bool, slen=6, newline:bool=False) -> str:
    while len(hdr) < slen+1:
        hdr+=' '
    if len(hdr) > slen:
        hdr = hdr[:slen]
    if   'info' in hdr.lower(): hdr=str(bcolors.HEADER  + hdr.upper() + bcolors.ENDC)
    elif 'warn' in hdr.lower(): hdr=str(bcolors.WARNING + hdr.upper() + bcolors.ENDC)
    elif 'fail' in hdr.lower(): hdr=str(bcolors.FAIL    + hdr.upper() + bcolors.ENDC)
    elif 'pass' in hdr.lower(): hdr=str(bcolors.OKGREEN + hdr.upper() + bcolors.ENDC)
    else: hdr=str(hdr.upper() + bcolors.ENDC)

    HDR = f"{hdr:{slen}s}"
    if hdr.strip() != "":
        HDR = HDR+":"
    FNAME = ""
    if show_func:
        stack_func = inspect.stack()[2].function
        if (stack_func.lower() not in ['<module>']):
            FNAME = "["+bcolors.BOLD  + f"{stack_func:s}()"+ bcolors.ENDC+"]"
    PRINT = f"{HDR:s} {FNAME:s} {msg:s}"
    while PRINT[-1] in ['\n']:
        PRINT = PRINT[:-1]
    if newline:
        PRINT = PRINT + "\n"
    print(PRINT)
    return escape_ansi(PRINT)

def SEPERATOR(msg:str="", msg_len=60, sep_len=80) -> str:
    msg=str(msg)
    if len(msg) > msg_len:
        msg=str(msg[:msg_len])
    if (len(msg) % 2) != 0:
        msg=str(msg)+' '

    msg = f"{bcolors.BOLD} {msg} {bcolors.ENDC}"
    while len(msg) < sep_len:
        msg = f"#{msg}#"
    print(msg)
    return escape_ansi(msg)

def INFO(msg:str="", hdr:str='INFO', show_func:bool=False, newline:bool=False) -> str:
    return DISPLAY(hdr, msg, show_func=show_func, newline=newline)

def WARNING(msg:str="", show_func:bool=True, newline:bool=False):
    return DISPLAY('WARN', msg, show_func=show_func, newline=newline)

def ERROR(msg:str="", show_func:bool=True, force_exit:bool=True) -> str:
    s = DISPLAY('FAIL', msg, show_func=show_func)
    if force_exit:
        print("Exiting...\n")
        sys.exit()
    return s

def SUCCESS(msg:str="", show_func:bool=False, newline:bool=True) -> str:
    return DISPLAY('PASS', msg, show_func=show_func, newline=newline)