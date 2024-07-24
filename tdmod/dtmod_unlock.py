import os
import telebot

# Substitua pelo seu token do Telegram
token = ""
chat_id = "" 
bot = telebot.TeleBot(token)
diretorio = "/sdcard/MT2/logs"

if not os.path.exists(diretorio):
    os.makedirs(diretorio)

arquivos_log = [f for f in os.listdir(diretorio) if f.endswith('.log')]

if arquivos_log:
    print(f"\nEnviando Payloads, aguarde...\n")
    payloads = []
    for arquivo_log in arquivos_log:
        filepath = os.path.join(diretorio, arquivo_log)
        with open(filepath, 'r') as file:
            for linha in file:
                if linha.strip().startswith('{"payload'):
                    payloads.append(linha.strip())
                    try:
                        bot.send_message(chat_id, linha.strip(), disable_web_page_preview=True)
                    except Exception as e:
                        #print(f"Erro ao enviar mensagem: {e}")
                        continue
        os.remove(filepath)  # Remove o arquivo após o envio
        print(f'Payloads extraidas com sucesso.\n')

    if payloads:
        # Criar e enviar o arquivo de payloads extraídos
        arquivo_payloads = "Payloads Extraidas.txt"
        with open(arquivo_payloads, 'w') as file:
            for payload in payloads:
                file.write(payload + '\n\n')  # Deixa uma linha em branco entre as linhas
        
        try:
            with open(arquivo_payloads, 'rb') as file:
                bot.send_document(chat_id, file)
            print("Arquivo de Payloads enviadao com sucesso! Verifique o bot no Telegram")
        except Exception as e:
            print(f"Erro ao enviar o arquivo: {e}")
        
        os.remove(arquivo_payloads)  # Remove o arquivo após o envio

else:
    bot.send_message(chat_id, "Logs não estão disponíveis.")
    print('Logs indisponíveis')
