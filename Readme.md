# Sistema de Conta Bancária

Este é um projeto simples de implementação de uma conta bancária em Python, desenvolvido com foco em testes unitários utilizando pytest.

## Funcionalidades

O sistema implementa as seguintes funcionalidades básicas de uma conta bancária:

- Consulta de saldo
- Depósito de valores
- Saque de valores
- Validações de operações

## Estrutura do Projeto

- `ContaBancaria.py`: Implementação da classe principal
- `ContaBancariaTest.py`: Testes unitários
- `README.md`: Documentação do projeto

## Classe ContaBancaria

A classe `ContaBancaria` possui os seguintes métodos:

- `get_saldo()`: Retorna o saldo atual da conta
- `depositar(valor)`: Realiza um depósito na conta
- `sacar(valor)`: Realiza um saque da conta
- `validarSaldo(valor)`: Valida se o valor do depósito é válido
- `validarSaque(valor)`: Valida se o saque pode ser realizado

## Testes Implementados

O projeto inclui os seguintes testes unitários:

1. `test_deve_ter_saldo_inicial_zero`: Verifica se o saldo inicial é zero
2. `test_deve_aumentar_saldo_apos_deposito_valido`: Testa depósito válido
3. `test_deve_retornar_uma_exception_apos_deposito_valido`: Testa depósito inválido
4. `test_deve_validar_saldo_apos_sacar_valor`: Testa operação de saque

## Como Executar

### Pré-requisitos
- Python 3.x
- pytest

### Executando os Testes
Para executar os testes, use o comando:
```bash
pytest ContaBancariaTest.py
```

## Regras de Negócio

1. O saldo inicial de qualquer conta é sempre zero
2. Não é possível realizar depósitos com valores negativos
3. Não é possível realizar saques maiores que o saldo disponível
4. Não é possível realizar saques com valores negativos
