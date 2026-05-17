import pytest
from parser import readFile
from exceptions import ParseError, ColumnNotFoundError


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        readFile('File doesn`t exist.csv')


def test_wrong_extension(tmp_path):
    test_file = tmp_path / "test.txt"

    with pytest.raises(ParseError):
        readFile(test_file)


def test_wrong_column(exist):
    with pytest.raises(ColumnNotFoundError):
        readFile(exist, column='price')


def test_returns_list(exist):
    assert readFile(exist) == ['3', '7', '6']
