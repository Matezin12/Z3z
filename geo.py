#print("estale os pacotes a seguir e depois volte  ")
#print("pip install requests,pkg python")

import os 
import requests

def get_ip_details(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "success":
        print("Detalhes do IP:")
        print(f"País: {data['country']}")
        print(f"Estado: {data['regionName']}")
        print(f"Provedor de Internet: {data['isp']}")
    else:
        print("Erro ao obter detalhes do IP.")

def main():
    ip = input("Digite o IP: ")
    get_ip_details(ip)

if __name__ == "__main__":
    main()


#Salve o código em um arquivo com extensão `.py`, por exemplo: `ip_details.py`. Para executá-lo, abra o aplicativo Termux e navegue até o diretório onde você salvou o arquivo Python. Use o comando `python ip_details.py` para executar o código.

#Lembre-se de que o Termux também tem algumas limitações em termos de acesso a recursos do sistema e permissões. Dependendo das restrições do seu dispositivo, você pode enfrentar problemas para acessar algumas informações de geolocalização específicas.