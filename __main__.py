import argparse

strategies = ['bfs', 'dfs', 'astr']
heuristics = ['hamm', 'manh']
order_char_list = ['L', 'R', 'U', 'D']


def isValid(w, k, input):
    numbers = set()
    counter = 0
    for i in input:
        counter += 1
        if len(i) != k:
            return False
        for number in i:
            numbers.add(number)
    if counter != w:
        return False
    for i in range(w * k):
        if i not in numbers:
            return False
    return True


def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--strategy', action='store', metavar='TYPE',
                        help="Chose the state search strategy: <bfs>, <dfs>, <astr>",
                        dest="strategy", type=str, required=True)

    parser.add_argument('-o', '--order', action='store', metavar='TYPE',
                        help="Chose the current state's search order if bfs or dfs was chosen e.g. LRUD",
                        dest="order", type=str)

    parser.add_argument('-he', '--heuristic', action='store', metavar='TYPE',
                        help="Chose heuristic for astr strategy.", dest="heuristic", type=str)

    parser.add_argument('-i', '--input', action='store', metavar='FILE',
                        help="Enter file that contains initial state of board: <file.txt>",
                        dest="inputFile", type=str, required=True)

    parser.add_argument('-so', '--solution', action='store', metavar='FILE',
                        help="Enter a file in which the solution will be written: <file.txt>",
                        dest="solutionFile", type=str, required=True)

    parser.add_argument('-st', '--stats', action='store', metavar='FILE',
                        help="Enter a file in which stats of solution will be written: <file.txt>",
                        dest="statsFile", type=str)

    args = parser.parse_args()

    if args.strategy not in strategies:
        print('Entered value of strategy is incorrect! It should be [-s] bfs, dfs or astr')
        exit(1)

    if args.strategy == strategies[2]:
        if args.heuristic not in heuristics:
            print('Astr strategy requires to define heuristic i.e. [-he] hamm or manh')
            exit(1)
        if args.order:
            print('Astr strategy uses heuristic so defined order was ignored.')
    else:
        if args.order is None:
            print('Bfs or dfs strategy requires to define search order i.e. [-o] LRUD or RUDL etc.')
            exit(1)
        if args.heuristic:
            print("Bfs or dfs doesn't need to define heuristic so it will be ignored.")

        if len(args.order) != 4 or all([char in order_char_list for char in args.order]) is False:
            print("Entered current state's neighbourhood search order is incorrect. It's for example [-o] RUDL "
                  "or LRUD etc.")
            exit(1)

    input = []
    w, k = 0, 0
    try:
        with open(args.inputFile, 'r') as file:
            w, k = [int(x) for x in next(file).split()]
            for line in file:
                input.append([int(x) for x in line.split()])

    except FileNotFoundError:
        print("No such file or directory: " + args.inputFile)
        exit(2)

    except ValueError:
        print("File " + args.inputFile + " contains mistakes. Check the content and correct it.")
        exit(3)

    if isValid(w, k, input) is False:
        print("File " + args.inputFile + " contains mistakes. Check the content and correct it.")
        exit(3)

    if args.solutionFile[-4:] != '.txt':
        print("Entered solution file must have .txt extension.")
        exit(4)

    if args.statsFile:
        if args.statsFile[-4:] != '.txt':
            print("Entered stats file must have .txt extension.")
            exit(4)


if __name__ == '__main__':
    parseArgs()
    print('elo')
