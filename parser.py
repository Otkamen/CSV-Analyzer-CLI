import csv
from pathlib import Path
from exceptions import ParseError, ColumnNotFoundError


def readFile(file: str | Path, column: str = 'category') -> list[str]:
    file = Path(file)
    result = []

    if file.suffix != '.csv':
        raise ParseError('File must be .csv')

    try:
        with file.open('r', encoding='utf-8') as old:
            reader = csv.DictReader(old)
            if column not in reader.fieldnames:
                raise ColumnNotFoundError(f"'{column}' not in file")
            for row in reader:
                result.append(row[column])

    except FileNotFoundError:
        raise FileNotFoundError(f'File {file} doesn`t found')

    return result
