from replit import clear


dicionario_codigo = {'11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', '16': 'F',
                     '21': 'G', '22': 'H', '23': 'I', '24': 'J', '25': 'K', '26': 'L',
                     '31': 'M', '32': 'N', '33': 'O', '34': 'P', '35': 'Q', '36': 'R',
                     '41': 'S/Z', '42': 'T', '43': 'U', '44': 'V/W', '45': 'X', '46': 'Y'
                     }

traducao_codigo = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', "É": "15", 'F': '16',
                     'G': '21', 'H': '22', 'I': '23',"Í": "23", 'J': '24', 'K': '25', 'L': '26',
                     'M': '31', 'N': '32', 'O': '33', 'P': '34', 'Q': '35', 'R': '36',
                     'S': '41', 'T': '42', 'U': '43','Ú': "43", 'V': '44', "W": "44", 'x': '45',
                     'y': '46', "Z": "41"
                     }

simbols = [",",'!', '?', '.', '%', '(', ')', '-', '+', " ", "\n"]

def decodificar_codigo(texto):
    codigo2 = texto.split()
    codigo_separado = []
    for c in range(0, len(codigo2)):
        for i in range(0,len(codigo2[c]), 2):
            try:
                codigo_separado.append(codigo2[c][i] + codigo2[c][i + 1] )
            except IndexError:
                codigo_separado.append(codigo2[c][i])
        codigo_separado.append(" ")
    

    traducao = []
    tradução2 = ""
    #ja consegue fazer a tradução
    for control in range(0, len(codigo_separado)):
        for chave, item in dicionario_codigo.items():
            if codigo_separado[control] == chave:
                traducao.insert(control, item)
                tradução2 += traducao[control]
                
            elif codigo_separado[control] in simbols:
                traducao.append(codigo_separado[control])
                tradução2 += traducao[control]
                break
            
    return tradução2

def codificar_codigo(texto):
    codigo = texto.upper()
    #print(codigo)
    # print(len(codigo))
    traducao = ""
    for controle in range(0, len(codigo)):
        for chave, item in traducao_codigo.items():
            if codigo[controle] == chave:
                traducao += item
            elif codigo[controle]  in simbols:
                traducao += codigo[controle]
                break

    return traducao