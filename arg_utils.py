
import argparse

def base_parser(display:bool=False, save:bool=False, verbose:bool=False) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument('-d',  '--display' , default=display, action=argparse.BooleanOptionalAction, help='display figures and graphics')
    parser.add_argument('-s',  '--save'    , default=save, action=argparse.BooleanOptionalAction, help='save output files')
    parser.add_argument('-v',  '--verbose' , default=verbose, action=argparse.BooleanOptionalAction, help='verbose output')

    return parser



if __name__ == "__main__":

    parser = base_parser()
    parser.add_argument('-f', '--file'     , required=True, type=str, help='path to element file')

    argdict = vars(parser.parse_args())
    print(argdict)