from Conta_Corrente import ContaCorrente,CartaoCredito



conta_lira = ContaCorrente("Lira",'111.222.333-45',-1000,10325,101168)

conta_maeLira = ContaCorrente("Beth",'222.333.444-55',5555,54682,656565656)

conta_lira.depositar_dinheiro(1000)
conta_lira.sacar_dinheiro(200)
conta_lira.transferir(400,conta_maeLira)

cartao_lira = CartaoCredito('Lira',conta_lira)
cartao_lira.numero = 146

print('Nome:', conta_lira._nome)
print('Cpf:', conta_lira._cpf)

conta_lira.consultar__saldo()

print('')

conta_lira.consultar_historico_transacoes()

print('Número da conta:(Verificado pelo cartão):',cartao_lira.conta_corrente._num_conta)
print('Número do cartão da conta Lira:',conta_lira._cartao[0].numero)
print('Informações do cartão:',cartao_lira.__dict__)

print(conta_lira._cartao)
help(ContaCorrente)