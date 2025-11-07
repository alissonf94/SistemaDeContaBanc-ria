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

def test_deve_retornar_uma_exception_apos_deposito_valido():

    conta = ContaBancaria()
    valor_deposito = -50.0

    with pytest.raises(ValueError) as excinfo:
        conta.depositar(valor_deposito)
    
    assert "Valor de depósito inválido." in str(excinfo.value)

def test_deve_validar_saldo_apos_sacar_valor():

    conta = ContaBancaria()
    valor_deposito = 200.0
    conta.depositar(valor_deposito)

    valor_saque = 50.0
    saldo_esperado = 150.0

    
    conta.sacar(valor_saque)

    assert conta.get_saldo() == saldo_esperado
