import sys
import inspect

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

def get_function_name():
    return inspect.stack()[1].function
