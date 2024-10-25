#objeto
from datetime import datetime
import pytz
from random import randint

class ContaCorrente():

    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
    Nome(str): Nome do cliente
    _cpf(str): CPF do cliente  
    saldo(str): Saldo dísponivel do cliente
    _limite(str): _limite de cheque especial daquele cliente
    num_conta(str): número da conta corrente do cliente
    _transacoes: as transações e suas respectivas datas feitas pelo cliente
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')
        
    def __init__(self,_nome,_cpf,_limite, _agencia, num_conta):
        self._nome = _nome
        self._cpf = _cpf
        self._saldo = 0
        self._limite = None
        self._agencia = _agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartao = []
    
    def consultar__saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))
        pass

    def depositar_dinheiro(self,valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self,valor):
        if self._saldo-valor <self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar__saldo()
            print('')
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo,ContaCorrente._data_hora()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        for transacao in self._transacoes:
            print(transacao)
        
class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self,titular,conta_corrente):
        self.numero = randint(1000,9999)
        self.titular = titular
        self.conta_corrente = conta_corrente
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month,CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        conta_corrente._cartao.append(self)












