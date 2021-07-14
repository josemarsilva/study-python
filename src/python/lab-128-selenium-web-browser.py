#
# filename   : lab-127-requests-beautifullsoap4-webscrapping.py
# Description:
# Docs       :
#               * https://pypi.org/project/selenium/
#               * https://sites.google.com/a/chromium.org/chromedriver/downloads
#               * https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.101/
# Required   :
#               * pip install selenium
#               * Chrome installed 91.0.4472.124 (Versão oficial) 64 bits
#               * Chrome Driver - WebDriver for Chrome
#               * wget https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_win32.zip
#               * sudo apt install unzip
#               # unzip chromedriver_win32.zip
#               # mv ./chromedriver_win32 ./study-python/src/python/
#

from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options = self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome( self.driver_path, options=self.options)

    def get_url(self, url):
        self.chrome.get(url)

    def click_btn_gerar_conta(self):
        try:
            btn_gerar_conta = self.chrome.find_element_by_id('btn_gerar_conta')
            btn_gerar_conta.click()
        except:
            print(f'ERROR at ChromeAuto.click_btn_gerar_conta(): ')
            return False
        # Default
        return True

    def get_tuple_conta(self):
        try:
            sleep(1)
            df_conta_corrente = self.chrome.find_element_by_id('conta_corrente').text
            df_agencia = self.chrome.find_element_by_id('agencia').text
            df_banco = self.chrome.find_element_by_id('banco').text
            df_cidade = self.chrome.find_element_by_id('cidade').text
            df_estado = self.chrome.find_element_by_id('estado').text
            tuple_conta = (df_conta_corrente, df_agencia, df_banco, df_cidade, df_estado)
            return tuple_conta
        except:
            print(f'ERROR at ChromeAuto.get_tuple_conta(): ')

    def script_conta(self):
        self.get_url('https://www.4devs.com.br/gerador_conta_bancaria')
        if self.click_btn_gerar_conta():
            return self.get_tuple_conta()

    def click_btn_gerar_pessoa(self):
        try:
            btn_gerar_pessoa = self.chrome.find_element_by_id('bt_gerar_pessoa')
            btn_gerar_pessoa.click()
        except:
            print(f'ERROR at ChromeAuto.click_btn_gerar_pessoa(): ')
            return False
        # Default
        return True

    def get_tuple_pessoa(self):
        try:
            sleep(1)
            df_nome = self.chrome.find_element_by_id('nome').text
            df_cpf = self.chrome.find_element_by_id('cpf').text
            df_rg = self.chrome.find_element_by_id('rg').text
            df_data_nasc = self.chrome.find_element_by_id('data_nasc').text
            df_sexo = self.chrome.find_element_by_id('sexo').text
            df_signo = self.chrome.find_element_by_id('signo').text
            df_mae = self.chrome.find_element_by_id('mae').text
            df_pai = self.chrome.find_element_by_id('pai').text
            df_email = self.chrome.find_element_by_id('email').text
            df_senha = self.chrome.find_element_by_id('senha').text
            df_cep = self.chrome.find_element_by_id('cep').text
            df_endereco = self.chrome.find_element_by_id('endereco').text
            df_numero = self.chrome.find_element_by_id('numero').text
            df_bairro = self.chrome.find_element_by_id('bairro').text
            df_cidade = self.chrome.find_element_by_id('cidade').text
            df_estado = self.chrome.find_element_by_id('estado').text
            df_telefone_fixo = self.chrome.find_element_by_id('telefone_fixo').text
            df_celular = self.chrome.find_element_by_id('celular').text
            df_altura = self.chrome.find_element_by_id('altura').text
            df_peso = self.chrome.find_element_by_id('peso').text
            df_tipo_sanguineo = self.chrome.find_element_by_id('tipo_sanguineo').text
            df_cor = self.chrome.find_element_by_id('cor').text
            tuple_pessoa = (df_nome, df_cpf, df_rg, df_data_nasc, df_sexo, df_signo, df_mae, df_pai, df_email, df_senha, df_cep, df_endereco, df_numero, df_bairro, df_cidade, df_estado, df_telefone_fixo, df_celular, df_altura, df_peso, df_tipo_sanguineo, df_cor )
            return tuple_pessoa
        except:
            print(f'ERROR at ChromeAuto.get_tuple_pessoa(): ')

    def script_pessoa(self):
        self.get_url('https://www.4devs.com.br/gerador_de_pessoas')
        if self.click_btn_gerar_pessoa():
            return self.get_tuple_pessoa()

    def quit(self):
        self.chrome.quit()



if __name__ == '__main__':

    # Max contas correntes e pessoas ...
    MAX_CONTA = 3
    MAX_PESSOA = 3

    # Instance Chrome WebDriver
    chrome = ChromeAuto()

    # Lista de conta corrente ...
    list_conta = []
    for i in range(MAX_CONTA):
        list_conta.append(chrome.script_conta())

    # Lista de pessoas ...
    list_pessoa = []
    for i in range(MAX_PESSOA):
        list_pessoa.append(chrome.script_pessoa())

    # Print data ...
    print(f'list_conta: ', list_conta)
    print(f'list_pessoa: ', list_pessoa)

    # Quit Chrome WebDriver ...
    chrome.quit()
