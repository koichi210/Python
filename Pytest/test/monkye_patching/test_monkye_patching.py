#import pytest
from main.get_path import GetPath
import os.path

def test_mytest(monkeypatch):
    def mockreturn(path):
        return 'C:\\Hogehoge'

    # Hook Method
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    x = GetPath().get_file_fullpath()
    assert x == 'C:\\Hogehoge'
