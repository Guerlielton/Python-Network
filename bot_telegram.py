import os
import requests
import json
from cisco_xr import route_xr
from cisco_xe import route_xe
from juniper import routepolicy
# from enviar_doc import arquivos
# from huawei import huawei_policy
# from vyos import vyos_policy
token = os.getenv("TELEGRAM_TOKEN")
class TelegramBot:
    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot{token}/'
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Olá bem vindo a configuração de policy :{os.linesep}1 - Juniper{os.linesep}2 - Cisco-XE{os.linesep}3 - Cisco-XR'''
        if mensagem == '1':
            routepolicy()
            return f'''Foi configurado o junos {os.linesep}Deseja sair?(s/n)
            '''
        elif mensagem == '2':
            route_xe()
            return f'''Foi configurado a routemap do Cisco XE{os.linesep}Deseja sair? (s/n)
            '''
        elif mensagem == '3':
            route_xr()
            return f'''Foi configurado a routemap do Cisco XR{os.linesep}Deseja sair? (s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            
            return ''' Obrigado a foi configuração realizada e esta acessivel em!'''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Obrigado a foi configuração realizada e esta acessivel em! '''
        else:
            return 'Gostaria de acessar o menu? Digite "menu"'

    # Responder
    def responder(self,resposta,chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)
    
bot = TelegramBot()
bot.Iniciar()