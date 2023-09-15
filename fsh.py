import socket
import os

print("              \033[31mS3S Z3Z\033[31m")
print("author:@__s4__s4")
# Função para obter os nomes de domínio correspondentes a um IP
def obter_nomes_dominio(ip):
    nomes_dom = []
    try:
        nome_dom = socket.gethostbyaddr(ip)[0]
        nomes_dom.append(nome_dom)
    except socket.herror:
        pass
    return nomes_dom

# Solicita ao usuário o nome do domínio
dominio = input(" \033[036m Digite o nome do domínio: \033[036m ")
os.system("clear")

# Obtém os IPs correspondentes ao domínio
ips = socket.gethostbyname_ex(dominio)[2]

# Imprime o domínio, IPs correspondentes e nomes de domínio
for ip in ips:
    nomes_dominio = obter_nomes_dominio(ip)
    for nome_dominio in nomes_dominio:
        print(f" \033[31m {dominio} -> \033[31m \033[036m {ip} -> {nome_dominio} \033[036m ")
        
