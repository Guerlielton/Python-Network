import os
import requests
import json
from networking.cisco_xe import route_xe
from networking.cisco_xr import route_xr
from networking.juniper import routepolicy

token = os.getenv('TELEGRAM_TOKEN')


class TelegramBot:
    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def start_polling(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem or mensagem.lower() in ('menu', 'Menu'):
            return f'''Olá, bem-vindo à configuração de policy:
1 - Juniper
2 - Cisco-XE
3 - Cisco-XR'''

        elif mensagem == '1':
            routepolicy()
            return f'''Foi configurado o Junos.
Deseja sair? (s/n)'''

        elif mensagem == '2':
            route_xe()
            return f'''Foi configurado a routemap do Cisco XE.
Deseja sair? (s/n)'''

        elif mensagem == '3':
            route_xr()
            return f'''Foi configurado a routemap do Cisco XR.
Deseja sair? (s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return 'Obrigado pela configuração realizada e está acessível em!'

        elif mensagem.lower() in ('n', 'não'):
            return 'Obrigado pela configuração realizada e está acessível em!'

        else:
            return 'Gostaria de acessar o menu? Digite "menu"'

    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.start_polling()
