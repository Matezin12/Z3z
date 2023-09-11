
import os
import re

os.system("clear")

def identificar_padroes_linguisticos(palavra):
    padrao_sul = re.compile(r'.*(tchê|Alçar a perna|Cacetinho|Embretar-se|Guri|Lindeiro|Solito|bah|uai|cuia|mate|porongo|tu).*', re.IGNORECASE)
    padrao_sudeste = re.compile(r'.*(uai|Bolado|Da hora|É fria|Larica|Quebrado|muié).*', re.IGNORECASE)
    padrao_nordeste = re.compile(r'.*(oxente|meu rei|meu bem|jumento|sertanejo|menininho|mulherona|arretado|arrumação|tô|bicho|mano|muié).*', re.IGNORECASE)
    padrao_norte = re.compile(r'.*(Moleque doido|Moscô|Égua|Borogodó|carimbó|igarapé|curro|ta ligado|bicudo|meno|parada).*', re.IGNORECASE)
    padrao_centro_oeste = re.compile(r'.*(Arruinou|Carreta|Empatar|peão|roça|boiadeiro|jacaré|capivara|piranha|buriti|pequi|jatobá|mermão|nois|muié|tô fazendo).*', re.IGNORECASE)
    
    # Adicione mais padrões linguísticos aqui, seguindo o mesmo padrão de regex
    
    regioes = []

    if re.match(padrao_sul, palavra):
        regioes.append("Região Sul: tchê, Alçar a perna, Cacetinho, Embretar-se, Guri, Lindeiro, Solito, bah, uai, cuia, mate, porongo, tu")
    
    if re.match(padrao_sudeste, palavra):
        regioes.append("Região Sudeste: uai, Bolado, Da hora, É fria, Larica, Quebrado, muié")
    
    if re.match(padrao_nordeste, palavra):
        regioes.append("Região Nordeste: oxente, meu rei, meu bem, jumento, sertanejo, menininho, mulherona, arretado, arrumação, tô falando, bicho, mano, muié")
    
    if re.match(padrao_norte, palavra):
        regioes.append("Região Norte: Moleque doido, Moscô, Égua, Borogodó, carimbó, igarapé, curro, ta ligado, bicudo, meno, parada")
    
    if re.match(padrao_centro_oeste, palavra):
        regioes.append("Região Centro-Oeste: Arruinou, Carreta, Empatar, peão, roça, boiadeiro, jacaré, capivara, piranha, buriti, pequi, jatobá, mermão, nois, muié, tô fazendo")
    
    # Adicione mais condições para outros padrões linguísticos
    
    if len(regioes) > 0:
        os.system("clear")
        return "Padrões linguísticos identificados:\n" + "\n".join(regioes)
    else:
        return "Padrão linguístico não identificado"

# Pergunta ao usuário qual é a palavra
palavra = input("Digite uma palavra a ser identificada: ")

# Identifica o padrão linguístico
resultado = identificar_padroes_linguisticos(palavra)

# Imprime o resultado
print("=================================================")
print(resultado)
print("=================================================")
    