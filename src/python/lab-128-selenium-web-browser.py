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
        try:
            sleep(1)
            df_conta_corrente = self.chrome.find_element_by_id('conta_corrente').text
            df_agencia = self.chrome.find_element_by_id('agencia').text
            df_banco = self.chrome.find_element_by_id('banco').text
            df_cidade = self.chrome.find_element_by_id('cidade').text
            df_estado = self.chrome.find_element_by_id('estado').text
            print(f'{df_banco} | {df_agencia} | {df_conta_corrente} | {df_cidade} | {df_estado}')
            #print(df_conta_corrente.get_attribute('innerHTML'))
        except:
            print(f'ERROR at ChromeAuto.click_btn_gerar_conta(): ')
            return False
        # Default
        return True

    def quit(self):
        self.chrome.quit()

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.get_url('https://www.4devs.com.br/gerador_conta_bancaria')
    if chrome.click_btn_gerar_conta():
        print(f'chrome.click_btn_gerar_conta()')
    #sleep(3)
    #chrome.get_url('https://www.4devs.com.br/gerador_de_pessoas')
    #sleep(1)
    chrome.quit()