import sys
import argparse as ap
from exceptions import ParseError, ColumnNotFoundError
from parser import readFile
from stats import writeFile, parseFile
from render import info, success, error


def parsed():
    parser = ap.ArgumentParser(description = 'CSV Analyzer')
    parser.add_argument('file')

    parser.add_argument(
        '--top',
        type = int,
        default = 5,
        help = 'Show top N categories'
    )
    parser.add_argument(
        '--output',
        type = str,
        default = 'report.txt',
        help = 'Output file path'
    )
    parser.add_argument(
        '--columns',
        type = str,
        default = 'category',
        help = 'Column to analyze'
    )

    return parser.parse_args()


def main():
    args = parsed()
    count = readFile(args.file, args.columns)
    parseData = parseFile(count)
    top = writeFile(parseData, args.top, args.output)
    sumAll = sum(parseData.values())
    return f'Top category: {top[0][0]} - {top[0][1] * 100 / sumAll:.2f}%'


if __name__ == '__main__':
    try:
        print(main())
    except (FileNotFoundError, ParseError, ColumnNotFoundError) as e:
        error(e)

