import pytest
from ContaBancaria import ContaBancaria

def test_deve_ter_saldo_inicial_zero():
    conta = ContaBancaria()
    assert conta.get_saldo() == 0.0

def test_deve_aumentar_saldo_apos_deposito_valido():

    conta = ContaBancaria()
    valor_deposito = 100.0

    
    conta.depositar(valor_deposito) 

    saldo_esperado = 100.0
    assert conta.get_saldo() == saldo_esperado