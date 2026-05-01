import csv
from exceptions import ParseError, ColumnNotFoundError


def readFile(file, column = 'category'):
    result = []
    if not file.endswith('.csv'):
        raise ParseError('File must be .csv')

    try:
        with open(file, 'r') as old:
            reader = csv.DictReader(old)
            if column not in reader.fieldnames:
                raise ColumnNotFoundError(f"'{column}' not in file")
            for row in reader:
                result.append(row[f'{column}'])

    except FileNotFoundError:
        raise FileNotFoundError(f'File {file} doesn`t found')

    return result
