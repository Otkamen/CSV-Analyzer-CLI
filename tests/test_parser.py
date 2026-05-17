import pytest
from parser import readFile
from exceptions import ParseError, ColumnNotFoundError


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        readFile('File doesn`t exist.csv')


def test_wrong_extension(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("num,category\n1,2\n")
    
    with pytest.raises(ParseError):
        readFile(str(test_file))


def test_wrong_column(tmp_path):
    test_file = tmp_path / "file_exist.csv"
    test_file.write_text("num,num,category\n1,2,3\n2,3,7\n3,5,6\n")
    
    with pytest.raises(ColumnNotFoundError):
        readFile(str(test_file), column='price')


def test_returns_list(tmp_path):
    test_file = tmp_path / "file_exist.csv"
    test_file.write_text("num,num,category\n1,2,3\n2,3,7\n3,5,6\n")
    
    assert readFile(str(test_file)) == ['3', '7', '6']
