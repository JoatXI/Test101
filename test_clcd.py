import pytest
from clcd import Motorbike

def test_motorbikes():
    bike = Motorbike("AWALA", 1590)
    
    assert bike.calculate_fee() == 3