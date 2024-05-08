
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', required=True, type=str, help='path to element file')

    argdict = vars(parser.parse_args())
    print(argdict)