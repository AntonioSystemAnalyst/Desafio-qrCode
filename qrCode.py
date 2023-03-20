def decodifica_qr_code (qrCode):
    textoClaro = '' # mensagem clara
    inicioLinha  = 0
    finalLinha   = 3
    for k in range (0, 10):
        
        linhas     = [] # forma uma única linha que contembra uma fileira de letras
        fragmento  = [] # recebe duas partes seguidas do codigo de uma letra
        letra      = [] # forma o código referente a uma letra
        frase      = [] # recebe o conjunto de letras
        
        razao      = 0 # define o valor a ser somado para encontrar o indice certo.
        
        if k < 2: # 2 primeiras partes onde tem o quadrado de posição do qrCode
            inicioColuna = 6
            finalColuna  = 30
            qtdTermos    = 24 # quantidade de numeros na linha
            qtdLetras    = 12 # quantidade de letras na linha
        else: # 8 partes seguintes, sem a presença do quadrado de posição do qrCode
            inicioColuna = 0
            finalColuna  = 30
            qtdTermos    = 30 # quantidade de numeros na linha
            qtdLetras    = 15 # quantidade de letras na linha

        
        for i in range (inicioLinha, finalLinha): # passando pelas colunas
            for j in range (inicioColuna, finalColuna): # passando pelas linhas
                linhas.append(qrCode[i][j]) # coloca num unico vetor, todos dados        
        
        
        for i in range (0, qtdTermos, 2): # quantidade de termos pega o espaçao de uma linha, a partir dela faz a resolução de 3 linhas
            for j in range (3):
                fragmento.append(linhas[i+razao])    # 1 termo do codigo 
                fragmento.append(linhas[i+razao+1])  # 2 termo do codigo
                letra.append(fragmento) # adiciona o trecho em letra
                fragmento = [] # limpar fragmento
                if k < 2: # razão varia por causa do quadrado
                    razao += 24
                else:
                    razao += 30
            frase.append(letra) # adicona a letra completa em frase
            letra = [] # limpar a letra
            razao = 0  # reseta a variavel de razão 
            
        for i in range (qtdLetras): # qtd de letras num determinado trecho, pode ser 12 ou 15, devido ao quadrado   
            for chave in c2m.keys(): # retorna a letra referente aquele codigo 
                if(frase[i] == c2m[chave]):
                    textoClaro += str(chave) # incremeta a frase encontrada a variavel textoClaro 
        
        inicioLinha  = finalLinha # inicio-linha recebe o numero que estava em final-lina, já que o range vai de zero até o numero-1 
        finalLinha   += 3 # soma tres ao valor da final-linha, contemplando as linhas que retornam a proxima frase 
        
    return textoClaro

qr = [[1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0],
      [1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1],
      [1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0],
      [1,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,1],
      [1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
      [0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
      [1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1],
      [0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
      [1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1],
      [1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1],
      [1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1],
      [0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
      [0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,1],
      [0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
      [0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1],
      [0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0],
      [0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
      [0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,0,1,1,1],
      [0,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1],
      [0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0,1],
      [0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0],
      [0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1],
      [0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0],
      [0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,0],
      [0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0],
      [1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0],
      [1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,1,1,0,0]]

c2m = {'a': [[0, 0], [0, 0], [0, 0]], 'b': [[0, 0], [0, 0], [0, 1]], 'c': [[0, 0], [0, 0], [1, 0]],
       'd': [[0, 0], [0, 0], [1, 1]], 'e': [[0, 0], [0, 1], [0, 0]], 'f': [[0, 0], [0, 1], [0, 1]],
       'g': [[0, 0], [0, 1], [1, 0]], 'h': [[0, 0], [0, 1], [1, 1]], 'i': [[0, 0], [1, 0], [0, 0]],
       'j': [[0, 0], [1, 0], [0, 1]], 'k': [[0, 0], [1, 0], [1, 0]], 'l': [[0, 0], [1, 0], [1, 1]],
       'm': [[0, 0], [1, 1], [0, 0]], 'n': [[0, 0], [1, 1], [0, 1]], 'o': [[0, 0], [1, 1], [1, 0]],
       'p': [[0, 0], [1, 1], [1, 1]], 'q': [[0, 1], [0, 0], [0, 0]], 'r': [[0, 1], [0, 0], [0, 1]],
       's': [[0, 1], [0, 0], [1, 0]], 't': [[0, 1], [0, 0], [1, 1]], 'u': [[0, 1], [0, 1], [0, 0]],
       'v': [[0, 1], [0, 1], [0, 1]], 'w': [[0, 1], [0, 1], [1, 0]], 'x': [[0, 1], [0, 1], [1, 1]],
       'y': [[0, 1], [1, 0], [0, 0]], 'z': [[0, 1], [1, 0], [0, 1]], '0': [[0, 1], [1, 0], [1, 0]],
       '1': [[0, 1], [1, 0], [1, 1]], '2': [[0, 1], [1, 1], [0, 0]], '3': [[0, 1], [1, 1], [0, 1]],
       '4': [[0, 1], [1, 1], [1, 0]], '5': [[0, 1], [1, 1], [1, 1]], '6': [[1, 0], [0, 0], [0, 0]],
       '7': [[1, 0], [0, 0], [0, 1]], '8': [[1, 0], [0, 0], [1, 0]], '9': [[1, 0], [0, 0], [1, 1]],
       ' ': [[1, 0], [0, 1], [0, 0]], '@': [[1, 0], [0, 1], [0, 1]], '/': [[1, 0], [0, 1], [1, 0]],
       ':': [[1, 1], [0, 0], [1, 1]], '+': [[1, 0], [1, 0], [0, 0]], '-': [[1, 0], [1, 0], [0, 1]],
       '*': [[1, 0], [1, 0], [1, 0]], '.': [[1, 0], [1, 0], [1, 1]], '%': [[1, 0], [1, 1], [0, 0]],
       '&': [[1, 0], [1, 1], [0, 1]], '#': [[1, 0], [1, 1], [1, 0]], '!': [[1, 0], [1, 1], [1, 1]],
       '?': [[1, 1], [0, 0], [0, 0]], ',': [[1, 1], [0, 0], [0, 1]], ';': [[1, 1], [0, 0], [1, 0]],
       '=': [[1, 1], [0, 1], [0, 0]], '[': [[1, 1], [0, 1], [0, 1]], ']': [[1, 1], [0, 1], [1, 0]],
       '{': [[1, 1], [0, 1], [1, 1]], '}': [[1, 1], [1, 0], [0, 0]], '(': [[1, 1], [1, 0], [0, 1]],
       ')': [[1, 1], [1, 0], [1, 0]], '$': [[1, 1], [1, 0], [1, 1]], '\\': [[1, 1], [1, 1], [0, 0]],
       '|': [[1, 1], [1, 1], [0, 1]], '<': [[1, 1], [1, 1], [1, 0]], '>': [[1, 1], [1, 1], [1, 1]]}


fraseOculta = decodifica_qr_code (qr)

print(fraseOculta) 

# eu nao temerei. eu enfrentarei meu medo. permitirei que ele passe atraves de mim. por onde o medo passou, nao havera mais nada. so eu restarei.a