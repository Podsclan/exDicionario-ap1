class Palavra:
	def _init_(self):
		self.palavra = ''
		self.sinonimo = ''
		self.classe = ''

def exibirMenu():
	print('\n ==== == MENU == ====')
	print('0 - SAIR')
	print('1 - CADASTRAR TERMO')
	print('2 - LISTAR TERMOS')
	print('3 - ADICIONAR NOVO SINONIMO')
	print('4 - MAIOR QTDD SINONIMO')
	print('5 - LISTAR POR CLASSE')
	print('6 - EXCLUIR TERMO')
	print('7 - EXCLUIR SINONIMO')
	print('==== == ==== == ====')

def cadastrarTermo(lista):
	novaPalavra = Palavra()
	palavra = input('Digite a palavra: ')
	palavraValida = validarPalavra(listaDicionario, palavra)
	if palavraValida == True:
		novaPalavra.palavra = palavra
		sinonimo = input('Digite os sinônimos: ')
		novaPalavra.sinonimo = sinonimo.split(';')
		novaPalavra.classe = input('Digite a classe gramatical: ')
		lista.append(novaPalavra)
		print('Palavra cadastrada com sucesso!')
	else:
		print('Palavra não cadastrada!')

def validarPalavra(lista, palavra):
	palavraValida = True
	for i in lista:
		if i.palavra == palavra:
			palavraValida = False
	return palavraValida

def listarTermo(lista):
	contadorTermo = 1
	contadorCaracteres = 0
	for i in lista:
		contadorSinonimo = 1
		print('Termo {}, tamanho de caracteres necessários para o termo: {}'.format(contadorTermo, len(i.palavra)))
		print('Palavra: {}'.format(i.palavra))
		print('Sinonimos: ')
		for j in i.sinonimo:
			print('{} - {}'.format(contadorSinonimo,j))
			contadorSinonimo+=1
		print('Classe gramatical: {}'.format(i.classe))
		contadorTermo+=1

def adicionarSinonimo(lista):
	termo = input('Digite o termo desejado para adicionar um sinonimo: ')
	for i in lista:
		if termo == i.palavra:
			print('Sinonimos do termo {}'.format(i.palavra))
			for j in i.sinonimo:
				print(j)
			novoSinonimo = input('Digite o sinonimo que deseja incluir: ')
			i.sinonimo.append(novoSinonimo)
			print('Lista de sinonimos atualizada: ')
			for j in i.sinonimo:
				print(j)

def listarMaiorQtddSinonimo(lista):
	maior = 0
	maiorTermo = ''
	for i in lista:
		if len(i.sinonimo) > maior:
			maior = len(i.sinonimo)
			maiorTermo = i.palavra
	print('O termo com maior quantidade de sinonimos é {} com {} sinonimos'.format(maiorTermo,maior))

def listarPorClasse(lista):
	classe = input('Digite a classe desejada: ')
	for i in lista:
		if i.classe == classe:
			print('Termo: {}'.format(i.palavra))
			print('Sinonimos: ')
			for j in i.sinonimo:
				print(j)
			print('Classe: {}'.format(classe))

def excluirTermo(lista):
	termo = input('Digite o termo que deseja excluir: ')
	for i in lista:
		if i.palavra == termo:
			listaDicionario.remove(i)

def excluirSinonimo(lista):
	termo = input('Digite o termo que deseja excluir: ')
	sinonimo = input('Digite o sinonimo que deseja excluir: ')
	for i in lista:
		if i.palavra == termo:
			for j in i.sinonimo:
				if j == sinonimo:
					i.sinonimo.remove(j)



listaDicionario = []

opc = -1
while opc != 0:
	exibirMenu()
	opc = int(input('Digite a opção:'))
	if opc == 1:
		cadastrarTermo(listaDicionario)
	elif opc == 2:
		listarTermo(listaDicionario)
	elif opc == 3:
		adicionarSinonimo(listaDicionario)
	elif opc == 4:
		listarMaiorQtddSinonimo(listaDicionario)
	elif opc == 5:
		listarPorClasse(listaDicionario)
	elif opc == 6:
		excluirTermo(listaDicionario)
	elif opc == 7:
		excluirSinonimo(listaDicionario)