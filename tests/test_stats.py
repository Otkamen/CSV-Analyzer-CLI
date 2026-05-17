from collections import Counter

from stats import parseFile, writeFile


def test_parseFile_counts_values():
    data = ['a', 'b', 'a', 'c', 'b', 'a']
    assert parseFile(data) == Counter({'a': 3, 'b': 2, 'c': 1})


def test_writeFile_writes_report_and_returns_top(tmp_path):
    counter = Counter({'a': 3, 'b': 2, 'c': 1})
    output_file = tmp_path / 'report.txt'

    result = writeFile(counter, top=2, output=output_file)

    assert result == [('a', 3), ('b', 2)]

    content = output_file.read_text()
    assert 'Top categories:' in content
    assert '1. a - 50.00%' in content
    assert '2. b - 33.33%' in content
