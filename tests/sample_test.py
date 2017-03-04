import pytest
import happiness

def test_evaluate_happiness():
    assert happiness.evaluate_happiness(9) == 'euphoric'
