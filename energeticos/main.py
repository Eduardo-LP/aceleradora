#--------inicializando o programa-------
tabelaEnergeticos = [['Empresa', 'Quantidade','ICMS','IPI','PIS','COFINS', 'Total']]
li = 1
loop = True

totalGeral = 0
totalMercado = 0
totalImpostos = 0

def mostraMatriz():
	print('')
	num = len(tabelaEnergeticos)
	for i in range(0,num):
		print(tabelaEnergeticos[i])

while loop == True:
	escolha = int(input('Digite 0 para sair e 1 para adicionar uma empresa: '))
	print('')
	if escolha == 0:
		loop = False
	elif escolha == 1:
		linha = []
		nome = str(input('Digite o nome da empresa: '))
		quantia = int(input('Digite a quantidade desejada: '))
		valor = quantia*4.5
		icms = (18/100)*valor
		ipi = (4/100)*valor
		pis = (1.86/100)*valor
		cofins = (8.54/100)*valor
		Total = valor + icms +  ipi + pis + cofins
		totalImpostos  = totalImpostos + (Total - valor)
		totalMercado = totalMercado + valor
		totalGeral = totalGeral + Total
		elemento = [nome, quantia, icms, ipi, pis, cofins, Total]
		for i in range(0, len(elemento)):
			linha.append(elemento[i])

		tabelaEnergeticos.append(linha)
		mostraMatriz()
		print(f'Total Impostos: {totalImpostos:.2f} \nTotal Mercadorias: {totalMercado:.2f} \nTotal Geral: {totalGeral:.2f}')
	else:
		print('Digite apenas 0 ou 1')
