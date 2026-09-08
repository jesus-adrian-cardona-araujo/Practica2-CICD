from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.sum(2, 3) == 5