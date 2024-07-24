import os
import requests

# Diretório de Downloads
downloads_dir = "/sdcard/Downloads"
apk_url = "https://github.com/LaelsonCG/scripts_termux/raw/main/tdmod/DTMod%20Unlock.apk"
script_url = "https://raw.githubusercontent.com/LaelsonCG/scripts_termux/main/tdmod/dtmod_unlock.py"
script_path = os.path.expanduser("~/dtmod_unlock.py")  # Diretório inicial do Termux

# Criar o diretório de Downloads se não existir
if not os.path.exists(downloads_dir):
    os.makedirs(downloads_dir)

# Função para baixar arquivos
def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Download concluído: {save_path}")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

# Baixar o APK necessário no diretório de Downloads
apk_path = os.path.join(downloads_dir, "DTMod Unlock.apk")
download_file(apk_url, apk_path)

# Baixar o script dtmod_unlock.py no diretório inicial do Termux
download_file(script_url, script_path)

# Solicitar token e chat_id do usuário
token = input('Envie o token do seu bot: ')
chat_id = input('Envie seu ID do telegram: ')

# Função para adicionar o token e chat_id no script dtmod_unlock.py
def configurar_script(script_path, token, chat_id):
    with open(script_path, 'r') as file:
        conteudo = file.read()
    
    conteudo = conteudo.replace('token = ""', f'token = "{token}"')
    conteudo = conteudo.replace('chat_id = ""', f'chat_id = "{chat_id}"')
    
    with open(script_path, 'w') as file:
        file.write(conteudo)
    
    print(f"\nConfigurações adicionadas no {script_path}\n")

# Adicionar o token e chat_id no script
configurar_script(script_path, token, chat_id)

# Avisar sobre a instalação
print('\nInstalado com sucesso\n\n')
print('O "DTMod Unlock.apk" foi baixado na pasta Downloads\n\n')
print('Use o MT manager para colocar as credenciais do app alvo no DTMod Unlock, instale o APK e em seguida, antes de abrir, dê permissões de armazenamento.\n\n')
print('Confira detalhes de como usar no grupo https://t.me/speednet_oficial')
