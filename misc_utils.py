import sys
import inspect
import re

def prompt_user_continue(msg:str="", exit_msg:str="", default_yes:bool=False):
    yes_no = '(y/[n])'
    continue_values = ['y', 'yes']
    if default_yes:
        yes_no = '([y]/n)'
        continue_values.append('')

    if msg.split() not in [""]: msg = f"{msg:s}\n"
    res = input(f"{msg}Continue? {yes_no:s} ")

    if res.lower() not in continue_values:
        if exit_msg.split() not in [""]: exit_msg = f"{exit_msg:s}\n"
        print(f"{exit_msg:s}Exiting...")
        sys.exit()

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m '
    BOLD      = '\033[1m '
    UNDERLINE = '\033[4m '

def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

def DISPLAY(TYPE:str, MSG:str, FNAME:str|None=None, slen=6):
    while len(TYPE) < slen:
        TYPE+=' '
    if len(TYPE) > slen:
        TYPE = TYPE[:slen]

    if   'info' in TYPE.lower(): TYPE=str(bcolors.HEADER  + TYPE.upper() + bcolors.ENDC)
    elif 'warn' in TYPE.lower(): TYPE=str(bcolors.WARNING + TYPE.upper() + bcolors.ENDC)
    elif 'fail' in TYPE.lower(): TYPE=str(bcolors.FAIL    + TYPE.upper() + bcolors.ENDC)
    elif 'pass' in TYPE.lower(): TYPE=str(bcolors.OKGREEN + TYPE.upper() + bcolors.ENDC)
    else: TYPE=str(TYPE.upper() + bcolors.ENDC)

    PRINT = f"{TYPE:{slen}s}: {MSG}"
    if FNAME is not None:
        PRINT = f"{TYPE:5s}: [{FNAME:s}()]  {MSG}"
    print(PRINT)
    return escape_ansi(PRINT)

def INFO(msg:str="", TYPE:str='INFO'):
    return DISPLAY(TYPE, msg, inspect.stack()[1].function)

def WARNING(msg:str=""):
    return DISPLAY('WARN', msg, inspect.stack()[1].function)

def ERROR(msg:str="", force_exit:bool=True):
    s = DISPLAY('FAIL', msg, inspect.stack()[1].function)
    if force_exit:
        print("Exiting...")
        sys.exit()
    return s

def SUCCESS(msg:str=""):
    return DISPLAY('PASS', msg, inspect.stack()[1].function)

def get_function_name():
    return inspect.stack()[1].function

if __name__ == "__main__":
    print(__file__)
