import pytest


@pytest.fixture
def exist(tmp_path):
    test_file = tmp_path / 'file_exist.csv'
    test_file.write_text("num,num,category\n1,2,3\n2,3,7\n3,5,6\n")
    return test_file