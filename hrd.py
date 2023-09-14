import os
import re
import time

os.system("clear")
time.sleep(3)
print(" ░█▀▀█ ─█▀█─ ░█▀▀▄ ░█▀▀█ ░█─░█ ▄█─") 　 
print(" ░█▄▄█ █▄▄█▄ ░█─░█ ░█─▄▄ ░█─░█ ─█─ ")　 
print(" ░█─── ───█─ ░█▄▄▀ ░█▄▄█ ─▀▄▄▀ ▄█▄ 　" 
print("  por:__s4___s4__ github                         v3.0")
def identificar_padroes_linguisticos(palavra):
    padrao_sul = re.compile(r'.*(tchê|Alçar a perna|Cacetinho|Embretar-se|Guri|Lindeiro|Solito|bah|uai|cuia|mate|porongo|tu).*', re.IGNORECASE)
    padrao_sudeste = re.compile(r'.*(uai|Bolado|Da hora|É fria|Larica|Quebrado|muié|).*', re.IGNORECASE)
    padrao_nordeste = re.compile(r'.*(oxente|meu rei|meu bem|jumento|sertanejo|menininho|mulherona|arretado|arrumação|tô|bicho|mano|muié).*', re.IGNORECASE)
    padrao_norte = re.compile(r'.*(Moleque doido|Moscô|Égua|Borogodó|carimbó|igarapé|curro|ta ligado|bicudo|meno|parada).*', re.IGNORECASE)
    padrao_centro_oeste = re.compile(r'.*(Arruinou|Carreta|Empatar|peão|roça|boiadeiro|jacaré|capivara|piranha|buriti|pequi|jatobá|mermão|nois|muié|tô fazendo).*', re.IGNORECASE)
    
    # Adicione mais padrões linguísticos aqui, seguindo o mesmo padrão de regex
    
    regioes = []

    if re.match(padrao_sul, palavra):
        regioes.append(" \033[0;32m Região Sul \033[0;32m ")
    
    if re.match(padrao_sudeste, palavra):
        regioes.append(" \033[0;32m Região Sudeste \033[0;32m ")
    
    if re.match(padrao_nordeste, palavra):
        regioes.append(" \033[0;32m Região Nordeste \033[0;32m ")
    
    if re.match(padrao_norte, palavra):
        regioes.append(" \033[0;32m Região Norte \033[0;32m ")
    
    if re.match(padrao_centro_oeste, palavra):
        regioes.append(" \033[0;32m Região Centro-Oeste \033[0;32m ")
    
    # Adicione mais condições para outros padrões linguísticos
    
    if len(regioes) > 0:
        os.system("clear")
        return " \033[31m Padrões linguísticos identificados: \033[31m \n" + "\n".join(regioes)
    else:
        return " \033[31m Padrão linguístico não identificado \033[31m "

# Pergunta ao usuário qual é a palavra
palavra = input(" \033[036m Digite uma palavra a ser identificada: \033[036m ")

# Identifica o padrão linguístico
resultado = identificar_padroes_linguisticos(palavra)

# Imprime o resultado
print(" \033[36m ================================= \033[36m ")
print(resultado)
print(" \033[36m ================================= \033[36m ")
