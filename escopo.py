#escopo global(declarada fora das funçoes e pode ser acessada dentro de qualqquer outras funçoes)
# e local(somente dentro da função declarada)

const_global ='Python' 

def escreve_texto ():
     const_local = 'Max mauro'
     print(f'Variavel global:{const_global}')
     print(f'Variavel local:{const_local}')

if __name__=='__main__':
    escreve_texto()

#
let_global = 'Aprendendo Python'
def aprendizado():
     global let_global
     let_global= 'Olá mundo!'
     print(f'varivale global: {let_global}')
if __name__== '__main__':
     aprendizado()

#por mais que tenha uma variavel global em operação, para alterar a variavel chamada com o mesmo nome deve
# criar ' global let_global' para atribuir/ trocar o valor da variavel fora da função(global) para uma de dentro da funçao
#sem criar uma nova, somente acessar o conteudo
