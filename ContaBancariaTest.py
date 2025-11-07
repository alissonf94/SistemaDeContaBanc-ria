import pytest
from ContaBancaria import ContaBancaria

def test_deve_ter_saldo_inicial_zero():
    conta = ContaBancaria()
    assert conta.get_saldo() == 0.0
