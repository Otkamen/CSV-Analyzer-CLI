import pytest
from render import success, info, error

def test_success_prints(capsys):
    success("done")
    out = capsys.readouterr().out
    assert "done" in out

def test_error_prints(capsys):
    error('ALARM')
    out = capsys.readouterr().out
    assert 'ALARM' in out

def test_info_prints(capsys):
    info('info')
    out = capsys.readouterr().out
    assert 'info' in out