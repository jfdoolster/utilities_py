
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-d',  '--display' , default=True, action=argparse.BooleanOptionalAction, help='display module figures')
    parser.add_argument('-s',  '--save'    , default=False, action=argparse.BooleanOptionalAction, help='save module figures')
    parser.add_argument('-v',  '--verbose' , default=False, action=argparse.BooleanOptionalAction, help='verbose output')
    parser.add_argument('-f', '--file'     , required=True, type=str, help='path to element file')

    argdict = vars(parser.parse_args())
    print(argdict)