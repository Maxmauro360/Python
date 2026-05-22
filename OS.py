#renomear todos os arquivos dentro de uma pasta, em massa.
import os

os.chdir('C:\\Teste')
print(f'diretório atual: {os.getcwd()}')

padrao_nome = input('Qual o nome do arquivo a ser usado (sem extensão)?:')

#fazer iteração por todos os itens que estao no diretorio e quando for o arquivo, ele renomeia

for contador, arq in enumerate(os.listdir()):
#extensão      nome
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + '' + str(contador + 1)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)
print(f'\n Arquivos renomeados!')