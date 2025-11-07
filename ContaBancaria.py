class ContaBancaria:
    def __init__(self):
       
        self.__saldo = 0.0

    def get_saldo(self) -> float:
        
        return self.__saldo

    def depositar(self, valor: float) -> None:
        if self.validarSaldo(valor):
            self.__saldo += valor
        else:
            raise ValueError("Valor de depósito inválido.")
    
    def validarSaldo(self, valor: float) -> None:
        if valor > 0:
            return True
        return False
    
    