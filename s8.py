#print("estale os pacotes a seguir e depois volte  ")
#print("pip install requests,pkg python")

import os 
import requests
os.system("clear")

def get_ip_details(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "success":
        print(" \033[31m            INFORMACOES OBTIDAS DO IP  \033[31m ")
        print(f" \033[32m País: {data['country']} \033[32m ")
        print(f" \033[35m Estado: {data['regionName']} \033[35m ")
        print(f" \033[33m Provedor de Internet: {data['isp']} \033[33m ")
    else:
        print(" \033[31m Erro ao obter detalhes do IP \033[31m ")

def main():
    ip = input(" \033[036m Digite o IP: \033[036m ")
    get_ip_details(ip)

if __name__ == "__main__":
    main()


#Salve o código em um arquivo com extensão `.py`, por exemplo: `ip_details.py`. Para executá-lo, abra o aplicativo Termux e navegue até o diretório onde você salvou o arquivo Python. Use o comando `python ip_details.py` para executar o código.

#Lembre-se de que o Termux também tem algumas limitações em termos de acesso a recursos do sistema e permissões. Dependendo das restrições do seu dispositivo, você pode enfrentar problemas para acessar algumas informações de geolocalização específicas.