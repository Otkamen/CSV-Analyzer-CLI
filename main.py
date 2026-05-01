import sys
import argparse as ap
from exceptions import ParseError, ColumnNotFoundError
from parser import readFile
from stats import writeFile, parseFile


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
    count = readFile(args.file)
    parse = parseFile(count)
    writeFile(parse)
    with open ('report.txt', 'r') as new:
        for row in new:
            if row.startswith('1.'): return f'Top category:{row[2:]}'


if __name__ == '__main__':
    try:
        print(main())
    except (FileNotFoundError, ParseError, ColumnNotFoundError) as e:
        print(f'Error: {e}')
