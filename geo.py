

















































































































































































































































#print("estale os pacotes a seguir e depois volte  ")
#print("pip install requests,pkg python")

import os 
import requests
import time

def progress_bar(done):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(1)


starting ()      
Progress: [####################
time.sleep("3")
os.system("clear") 
time.sleep("2")    
print("         Z3Z G30         ")
print("                          ")
print("░░░░░░███████ ]▄▄▄▄▄▄▄▄")
print("▂▄▅█████████▅▄▃▂")
print("I███████████████████]")
print("◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...")
print("                          ")    
time.sleep("6")
def get_ip_details(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "success":
        print(" \033[31m            INFORMACOES OBTIDAS DO IP  \033[31m ")
        print(f" \033[32m País: {data['country']} \033[32m ")
        print(f" \033[33m Estado: {data['regionName']} \033[33m ")
        print(f" \033[036m Provedor de Internet: {data['isp']} \033[036m ")
    else:
        print(" \033[31m Erro ao obter informações  do IP \033[31m ")

def main():
    ip = input(" \033[036m Digite o IP: \033[31m ")
    get_ip_details(ip)

if __name__ == "__main__":
    main()


#Salve o código em um arquivo com extensão `.py`, por exemplo: `ip_details.py`. Para executá-lo, abra o aplicativo Termux e navegue até o diretório onde você salvou o arquivo Python. Use o comando `python ip_details.py` para executar o código.

#Lembre-se de que o Termux também tem algumas limitações em termos de acesso a recursos do sistema e permissões. Dependendo das restrições do seu dispositivo, você pode enfrentar problemas para acessar algumas informações de geolocalização específicas.
