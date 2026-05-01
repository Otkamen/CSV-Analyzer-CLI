import csv
from exceptions import ParseError, ColumnNotFoundError


def readFile(file):
    result = []
    if not file.endswith('.csv'):
        raise ParseError('File must be .csv')

    try:
        with open(file, 'r') as old:
            reader = csv.DictReader(old)
            if 'category' not in reader.fieldnames:
                raise ColumnNotFoundError("'category' not in file")
            for row in reader:
                result.append(row['category'])

    except FileNotFoundError:
        raise FileNotFoundError(f'File {file} doesn`t found')

    return result
