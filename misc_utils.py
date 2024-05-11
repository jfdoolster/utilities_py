import sys

def prompt_user_continue(msg=str or None, exit_msg=""):
    if msg not in [None, ""]: print(f"{msg}")
    res = input(f"Continue? (y/[n]) ")
    if res.lower() not in ['y', 'yes']:
        if exit_msg not in [None, ""]: print(f"{exit_msg}")
        print("Exiting...")
        sys.exit()


if __name__ == "__main__":
    print(__file__)
