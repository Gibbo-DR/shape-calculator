from shape_calculator import *
import pytest

def test_cuboid_A(): #5
    data = Cuboid(500,200,200)
    assert "Volume = 20000000mm^3" in data
    assert "surface area = 480000mm^2" in data
    assert "H:W = 2.5" in data
    assert "W:L = 1" in data
    assert "L:H = 0.4" in data

def test_cuboid_B(): #5
    data = Cuboid(10,11,10000)
    assert "Volume = 1100000mm^3" in data
    assert "surface area = 420220mm^2" in data
    assert "H:W = 0.909" in data
    assert "W:L = 0.001" in data
    assert "L:H = 1000.0" in data

def test_measurementfunc(monkeypatch,capsys):
    main()
    # monkeypatch.setattr('builtins.input', lambda _: "3")
    # monkeypatch.setattr('builtins.input', lambda _: "50")
    getMeasurement().input
    captured = capsys.readouterr()
    assert captured.out == "Volume = 523598.776mm^3,\
            \nsurface area = 31415.927mm^2"