import pytest
from main import topla

def test_toplama_islemi():
    assert topla(2, 3) == 5, "HATA: 2+3 işlemi 5 etmeliydi!"
    assert topla(-1, 1) == 0, "HATA: -1+1 işlemi 0 etmeliydi!"
    assert topla(10, 10) == 20, "HATA: 10+10 işlemi 20 etmeliydi!"