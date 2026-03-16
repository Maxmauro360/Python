# nome = 'Max '
# letra = nome [1]
# print(letra) 
# frase = "curso de python aqui"
# frase1 = 'MAX'
# palavras = frase.split()
# print(palavras)
# for letra in frase1:
#      print(letra)

# email = input('Digite seu email:')
# arroba = email.find('@') #encontra dentro da string este caracter
#print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:] #da proxima prosição depois do @
#print(usuario)
#print(dominio)

# 

# objeto_celete = 'galáxia Celestial'
# print(objeto_celete.upper()) #upper escreve em maisculo
# print(objeto_celete.lower()) #lower escreve em minusculo
# print(objeto_celete.capitalize()) #capitalize escreve primiera letra em maiusculo
# print(objeto_celete.title()) #title escreve cadad letra de cada palavra em maiusculo


# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco') #se for algo que não consiga mudar
#                                                        #ele coloca outro nome
# print(suplemento)
# print(n_suplemento)


# frase = '                         bife de fígado faz bem' #funçoes que eliminam espaço
# print(frase)
# print(frase.lstrip) #l de left
# print(frase.rstrip)# r de right
# print(frase.strip) # esquerda tanto direita

#alinhaento de texto pra exibiçao

# fruta = 'abacaxi'
# print(fruta) #a esquerda
# print(fruta.rjust(20)) # a direita
# print(fruta.center(20)) # no centro
# print(fruta.ljust(20, '-')) #a esquerda
# print(fruta.center(20,"-"))

p = 'Max Mauro'
print(p.startswith('M'))
print(p.endswith('o'))

#docstrings
#espécie de documentação que pode ser insserido em algum algum modulo, função ou classe...
#não é interpretadoa como comando

texto = """" não use esse tipo comentários

Docstring"""

